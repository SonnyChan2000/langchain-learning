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
        {"role": "system", "content": "你是一个温柔鼓励人的职业规划师，说话像朋友聊天，爱用比喻"},
        {"role": "user","content":"我刚学会python基础, 能找到工作吗？"}
    ]
)

answer = response.choices[0].message.content
print(answer)