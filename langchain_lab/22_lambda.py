import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableLambda
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

llm = ChatOpenAI(
    api_key=os.getenv("ZHIPU_API_KEY"),
    model="glm-4-flash",
    base_url="https://open.bigmodel.cn/api/paas/v4",
)

def 加工(x):
    clean = str(x).strip()
    n = len(clean)
    return f"[内容长度{n}字]\n{clean}"


prompt = ChatPromptTemplate.from_messages([
    ("system", "你是文案助手, 用一句话介绍Python"),
    ("user", "请输出"),
])

chain = prompt | llm | StrOutputParser()
output = chain.invoke({})

print("---- 模型原始输出 ----")
print(output)
print("---- 加工后 ----")
print(加工(output))