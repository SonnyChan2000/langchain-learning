import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

llm = ChatOpenAI(
    api_key=os.getenv("ZHIPU_API_KEY"),
    model="glm-4-flash",
    base_url="https://open.bigmodel.cn/api/paas/v4",
)

translate_prompt = ChatPromptTemplate.from_messages([
    ("system", "你是专业翻译, 把中文翻译成英文, 只输出译文"),
    ("user", "{文本}"),
])
translate_chain = translate_prompt | llm | StrOutputParser()

polish_prompt = ChatPromptTemplate.from_messages([
    ("system", "你是文字编辑, 把输入的英文改写成更优美的3句话"),
    ("user", "{文本}"),
])

polish_chain = polish_prompt | llm | StrOutputParser()

中文 = "科技创新让生活更美好。"
英文 = translate_chain.invoke({"文本": 中文})
润色 = polish_chain.invoke({"文本": 英文})

print("原文: ", 中文)
print("译文: ", 英文)
print("润色结果:")
print(润色)