import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.agents import create_agent
from langchain.tools import tool

load_dotenv()

llm = ChatOpenAI(
    api_key=os.getenv("ZHIPU_API_KEY"),
    model="glm-4-flash",
    base_url="https://open.bigmodel.cn/api/paas/v4"
)

@tool
def add(a: int, b: int) -> int:
    """将两个整数相加。适用于加法计算。传入a 和 b, 返回a + b的结果。"""
    return a + b

@tool
def multiply(a: int, b: int) -> int:
    """将两个整数相乘。适用于乘法计算。传入a 和 b, 返回a 乘 b的结果。"""
    return a * b

agent = create_agent(model=llm, tools=[add, multiply], system_prompt="你是计算助手, 能使用加法和乘法工具。根据问题选择正确的工具, 得到结果后直接告诉用户答案。",)

print("=== 测试1: 加法 ===")
r1 = agent.invoke({"messages": [{"role": "user", "content": "12 + 34 = ?"}]})
print(r1["messages"][-1].content)

print("\n=== 测试2: 乘法 ===")
r2 = agent.invoke({"messages": [{"role": "user", "content": "12 x 34 = ?"}]})
print(r2["messages"][-1].content)