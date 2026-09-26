# 给create_agent加敏感工具审批闸口
import os
from dotenv import load_dotenv
from langchain.agents import create_agent
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.types import Command
from langchain_core.tools import tool
from langchain_openai import ChatOpenAI

load_dotenv()

@tool
def 转账(收款人: str, 金额: float) -> str:
    """给指定收款人转账指定金额(敏感操作)。"""
    return f"已向{收款人}转账{金额}元"

llm = ChatOpenAI(
    model="glm-4-flash",
    api_key=os.getenv("ZHIPU_API_KEY"),
    base_url="https://open.bigmodel.cn/api/paas/v4"
)

agent = create_agent(model=llm, tools=[转账], checkpointer=InMemorySaver())

config = {"configurable": {"thread_id": "转账流程"}}

print(">> 发起转账请求...")
result = agent.invoke(
    {"messages" : [("user", "给张三转1000元")]},
    config,
    interrupt_before=["tools"],
)
print(">> Agent已暂停, 待执行的工具调用:")
最后消息 = result["messages"][-1]
if 最后消息.tool_calls:
    print("Agent想调用的工具:", 最后消息.tool_calls)
else:
    print("Agent未调用工具")

决定 = input("批准这笔转账吗? 输入 approve/reject: ")

if 决定 == "approve":
    final = agent.invoke(Command(resume="approve"), config)
    print(">> 已批准, 执行结果:")
    print(final["messages"][-1].content)
else:
    agent.invoke(Command(resume="reject"), config)
    print(">> 已驳回, 转账未执行")
