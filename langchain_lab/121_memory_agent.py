import os
from dotenv import load_dotenv
load_dotenv()
from typing import Annotated
from typing_extensions import TypedDict
from langchain_openai import ChatOpenAI
from langchain.tools import tool
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode
from langgraph.checkpoint.memory import InMemorySaver
from langchain_core.messages import HumanMessage

# 工具
@tool
def 加法(x: int, y: int) -> int:
    """计算两个整数 x + y 的和"""
    return x + y

tools = [加法]

# 模型
llm = ChatOpenAI(model="glm-4-flash", api_key=os.getenv("ZHIPU_API_KEY"),
                 base_url="https://open.bigmodel.cn/api/paas/v4", temperature=0.3)
model = llm.bind_tools(tools)

# State(messages 追加)
class State(TypedDict):
    messages: Annotated[list, add_messages]

# 节点 + 判断函数
def 调用模型(state: State):
    return {"messages": [model.invoke(state["messages"])]}

tool_node = ToolNode(tools)

def 是否继续(state:State) -> str:
    if state["messages"][-1].tool_calls:
        return "tools"
    return "END"

# 拼装成图 + 挂 checkpointer
builder = StateGraph(State)
builder.add_node("agent", 调用模型)
builder.add_node("tools", tool_node)
builder.add_edge(START, "agent")
builder.add_conditional_edges("agent", 是否继续, {"tools": "tools", "END": END})
builder.add_edge("tools", "agent")

checkponiter = InMemorySaver()
graph = builder.compile(checkpointer=checkponiter)

# 测试:同一 thread 多轮对话
config = {"configurable": {"thread_id": "我的会话"}}

print("===== 第一轮 =====")
结果1 = graph.invoke({"messages": [HumanMessage(content="你好, 我叫Bob")]}, config)
print("Agent:", 结果1["messages"][-1].content)

print("===== 第二轮 =====")
结果2 = graph.invoke({"messages": [HumanMessage(content="我叫什么名字?")]}, config)
print("Agent:", 结果2["messages"][-1].content)