import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

llm = ChatOpenAI(
    api_key=os.getenv("ZHIPU_API_KEY"),
    model="glm-4-flash",
    base_url="https://open.bigmodel.cn/api/paas/v4",
    temperature=0.7
)

resp = llm.invoke("用一句话介绍Langchain")

print(resp.content)