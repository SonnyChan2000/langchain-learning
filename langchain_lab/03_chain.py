import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

llm = ChatOpenAI(
    api_key=os.getenv("ZHIPU_API_KEY"),
    model="glm-4-flash",
    base_url="https://open.bigmodel.cn/api/paas/v4",
)

prompt = ChatPromptTemplate.from_messages([
    ("system", "你是一名专业的{语言}翻译"),
    ("user", "请翻译这段话: {文本}")
])



chain = prompt | llm

resp = chain.invoke({"语言": "英文", "文本": "今天天气真不错"})
print(resp.content)

resp2 = chain.invoke({"语言": "中文", "文本": resp.content})
print(resp2.content)