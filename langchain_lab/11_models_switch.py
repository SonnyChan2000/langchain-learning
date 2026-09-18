import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

zhipu = ChatOpenAI(
    api_key=os.getenv("ZHIPU_API_KEY"),
    model="glm-4-flash",
    base_url="https://open.bigmodel.cn/api/paas/v4",
)

for i in range(2):
    resp = zhipu.invoke("用一句话解释什么是langchain")
    print(f"第{i + 1}次: {resp.content}")

