import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("ZHIPU_API_KEY"),
    base_url="https://open.bigmodel.cn/api/paas/v4/"
)

messages = [
    {"role": "system", "content": "你是一个乐于助人的AI助手, 回答简洁友好"}
]

print("="*40)
print("AI聊天机器人(流式版)")
print("输入quit退出, 输入clear清空对话")
print("="*40)

while True:
    user_input = input("\n你: ").strip()

    if user_input == "quit":
        print("再见!")
        break
    if user_input == "clear":
        messages = [messages[0]]
        print("对话已清空")
        continue
    if not user_input:
        continue

    messages.append({"role": "user", "content": user_input})

    try:
        print("AI: ", end="")
        stream = client.chat.completions.create(
            model="glm-4-flash",
            messages=messages,
            stream=True
        )

        full_answer = ""
        for chunk in stream:
            delta = chunk.choices[0].delta
            if delta.content:
                print(delta.content, end="", flush=True)
                full_answer += delta.content
        print()

        messages.append({"role": "assistant", "content": full_answer})

    except Exception as e:
        print(f"\n出错了: {e}")
        messages.pop()    
        