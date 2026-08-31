import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("ZHIPU_API_KEY"),
    base_url="https://open.bigmodel.cn/api/paas/v4/"
)

response = client.chat.completions.create(
    model="glm-4-flash",
    messages=[
        {"role": "system", "content": "你是一个乐于助人的AI助手"},
        {"role": "user", "content": "你好"}
    ]
)

print("回复: ", response.choices[0].message.content)
print()
print("Token用量: ", response.usage)
