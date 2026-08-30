import os 
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("ZHIPU_API_KEY"),
    base_url="https://open.bigmodel.cn/api/paas/v4"
)

messages = [
    {"role": "system", "content":"你是一个乐于助人的AI助手, 回答简洁友好"}
]

print("AI助手已启动, 输入quit退出")
while True:
    user_input = input("你: ").strip()
    if user_input == "quit":
        print("再见!")
        break

    messages.append({"role": "user", "content": user_input})

    response = client.chat.completions.create(
        model="glm-4-flash",
        messages=messages
    )

    answer = response.choices[0].message.content
    print(f"AI: {answer}")

    messages.append({"role": "assistant", "content": "answer"})
    