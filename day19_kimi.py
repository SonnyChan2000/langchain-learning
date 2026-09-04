import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("MOONSHOT_API_KEY"),
    base_url="https://api.moonshot.cn/v1"
)

response = client.chat.completions.create(
    model="kimi-k2.6",
    messages=[
        {"role": "system", "content": "你是kimi, 由Moonshot AI 提供的人工智能助手。"},
        {"role": "user", "content": "你好, 请用一句话介绍自己。"}
    ]
)

print(response.choices[0].message.content)