import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.agents import create_agent
from langgraph_supervisor import create_supervisor
from langchain_core.tools import tool

load_dotenv()

llm = ChatOpenAI(
    model="glm-4-flash",
    api_key=os.getenv("ZHIPU_API_KEY"),
    base_url="https://open.bigmodel.cn/api/paas/v4"

)

@tool
def 查资料(主题: str) -> str:
    """当任务需要查找知识、资料、文献时调用。"""
    return f"查到关于'{主题}'的资料: 这是相关资料摘要..."

@tool
def 算总账(单价: float, 数量: int) -> str:
    """当任务需要计算总价时调用。"""
    return f"总价为{单价 * 数量:.2f}元"

研究员 = create_agent(
    model=llm,
    tools=[查资料],
    system_prompt="你是资料研究员, 专门负责查找和汇总资料, 只做资料相关的事。",
    name="研究员"
)

核算员 = create_agent(
    model=llm,
    tools=[算总账],
    system_prompt="你是财务核算员,专门负责算账,只做计算相关的事。",
    name="核算员"
)

supervisor = create_supervisor(
    agents=[研究员, 核算员], model=llm,
    prompt=("你是一个项目主管, 手下有两个专家: 研究员负责查资料, 核算员负责算账。"
            "根据用户的请求, 判断该派给哪个专家, 必要时可让多个专家协作。"),
    ).compile(name="主管")


result = supervisor.invoke({"messages": [("user","查一下人工智能的现状, 然后算一下买10件单价50元的货要多少钱")]})
print(result["messages"][-1].content)