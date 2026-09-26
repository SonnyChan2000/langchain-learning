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

# 1.定义两个工具
@tool
def 加法(x: int, y: int) -> int:
    """计算两个整数x + y的和"""
    return x + y

@tool
def 查今日菜谱(口味: str) -> str:
    """根据口味推荐一道今天的菜谱"""
    食谱 = {"清淡": "清蒸鲈鱼", "辣": "麻婆豆腐", "甜": "糖醋里脊"}
    return f"今日(口味)菜谱推荐: {食谱.get(口味, '家常小炒')}"

tools = [加法, 查今日菜谱]

# 2.模型绑定工具(智谱)
llm = ChatOpenAI(model="glm-4-flash", api_key=os.getenv("ZHIPU_API_KEY"),
                 base_url="https://open.bigmodel.cn/api/paas/v4", temperature=0.3)
model = llm.bind_tools(tools)

# 3.State:messages追加
class State(TypedDict):
    messages: Annotated[list, add_messages]

# 4.两个节点 + 判断函数
def 调用模型(state: State):
    return {"messages": [model.invoke(state["messages"])]}

tool_node = ToolNode(tools)

def 是否继续(state: State) -> str:
    if state["messages"][-1].tool_calls:
        return "tools"
    return "END"

# 5.拼装成图
builder = StateGraph(State)
builder.add_node("agent", 调用模型)
builder.add_node("tools", tool_node)
builder.add_edge(START, "agent")
builder.add_conditional_edges("agent", 是否继续, {"tools": "tools", "END": END})
builder.add_edge("tools", "agent")
graph = builder.compile()

# 6.测试
from langchain_core.messages import HumanMessage
for 问题 in ["3 + 5等于多少?", "今天想吃点辣的, 推荐个菜", "你好啊"]:
    print(f"\n================= 用户问: {问题} =============")
    结果 = graph.invoke({"messages": [HumanMessage(content=问题)]})
    print("最终回答:", 结果["messages"][-1].content)
    print("完整执行消息数:", len(结果["messages"]))