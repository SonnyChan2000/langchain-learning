import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("DASHSCOPE_API_KEY"),
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
)

question = "用三句话解释什么是大模型API"

for temp in[0.0, 0.9]:
    print(f"\n===== temperature={temp} =====")
    response = client.chat.completions.create(
        model="qwen-plus",
        messages=[
            {"role": "system", "content": "你是一个乐于助人的AI助手"},
            {"role": "user", "content":question}],
        temperature = temp
    )
    print(response.choices[0].message.content)
