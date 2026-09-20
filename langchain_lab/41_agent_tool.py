import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.tools import tool
from langchain.agents import create_agent

load_dotenv()

llm = ChatOpenAI(
    api_key=os.getenv("ZHIPU_API_KEY"),
    model="glm-4-flash",
    base_url="https://open.bigmodel.cn/api/paas/v4"
)

@tool
def add(a: int, b: int) -> int:
    """将两个整数相加, 适用于任何加法计算。传入a和b, 返回a + b的结果。"""
    return a + b

agent = create_agent(model=llm, tools=[add], system_prompt="你是一个乐于帮助的计算助手, 能使用工具。需要计算时调用工具, 得到结果后直接告诉用户答案。",)


结果 = agent.invoke({"messages": [{"role": "user", "content": "请帮我计算123加456等于多少?"}]})
print(结果["messages"][-1].content)

