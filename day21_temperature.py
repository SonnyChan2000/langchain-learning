import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("ZHIPU_API_KEY"),
    base_url="https://open.bigmodel.cn/api/paas/v4"
)

prompt = "给奶茶店起一个名字, 只输出名字本身。"

print("="*10 + "temperature=0" + "="*10)
for i in range(3):
    r = client.chat.completions.create(
        model="glm-4-flash",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.0
    )
    print(f"第{i + 1}次: {r.choices[0].message.content}")

print("\n" + "="*10 + "temperature=1(最放飞)" + "="*10)
for i in range(3):
    r = client.chat.completions.create(
        model="glm-4-flash",
        messages=[{"role": "user", "content": prompt}],
        temperature=1
    )
    print(f"第{i+1}次: {r.choices[0].message.content}")