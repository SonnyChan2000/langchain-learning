import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.agents import create_agent
from langchain.tools import tool

load_dotenv()

llm = ChatOpenAI(
    api_key=os.getenv("ZHIPU_API_KEY"),
    model="glm-4-flash",
    base_url="https://open.bigmodel.cn/api/paas/v4",
)

@tool
def multiply(a: int, b: int) -> int:
    """将两个整数相乘。适用于乘法计算。传入a 和 b。"""
    return a * b

# 不带工具的LLM(直接问)
print("=== 场景1: 不带工具, 直接让模型心算 ===")
问题 = "请精确计算 123456789 x 987654321 等于多少"
肉算 = llm.invoke(问题).content
print("模型回答: ", 肉算)

# 带工具的Agent
agent = create_agent(model=llm, tools=[multiply], system_prompt="你是计算助手, 设计乘法时务必调用工具, 不要心算。",)
print("\n=== 场景2: Agent 带工具计算 ===")
r = agent.invoke({"messages": [{"role": "user", "content": 问题}]})
print("Agent 回答: ", r["messages"][-1].content)