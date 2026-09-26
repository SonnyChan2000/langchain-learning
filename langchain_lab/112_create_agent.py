import os
from dotenv import load_dotenv
load_dotenv()
from langchain_openai import ChatOpenAI
from langchain.tools import tool
from langchain.agents import create_agent
from langchain_core.messages import HumanMessage

@tool
def 加法(x: int, y: int) -> int:
    """计算两个整数 x + y 的和"""
    return x + y

@tool
def 查今日菜谱(口味: str) -> str:
    """根据口味推荐一道今天的菜谱"""
    食谱 = {"清淡": "清蒸鲈鱼", "辣": "麻婆豆腐", "甜": "糖醋里脊"}
    return f"今日{口味}菜谱推荐: {食谱.get(口味, '家常小炒')}"

llm = ChatOpenAI(model="glm-4-flash", api_key=os.getenv("ZHIPU_API_KEY"),
                base_url="https://open.bigmodel.cn/api/paas/v4/", temperature=0.3)

agent = create_agent(model=llm, tools=[加法, 查今日菜谱])

for 问题 in ["3 + 5等于多少?", "今天想吃点辣的, 推荐个菜"]:
    print(f"\n =====用户问: {问题} =====")
    结果 = agent.invoke({"messages": [HumanMessage(content=问题)]})
    print("最终回答:", 结果["messages"][-1].content)