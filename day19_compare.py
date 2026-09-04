import os
import time
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

zhipu_client = OpenAI(
    api_key=os.getenv("ZHIPU_API_KEY"),
    base_url="https://open.bigmodel.cn/api/paas/v4/"
)
kimi_client = OpenAI(
    api_key=os.getenv("MOONSHOT_API_KEY"),
    base_url="https://api.moonshot.cn/v1"
)

question = "用三句话解释什么是大模型的Function Calling"

# ===== 对比1：回答质量 + 响应速度 =====
print("=" * 50)
print("【智谱 GLM-4-Flash】")
t1 = time.time()
r1 = zhipu_client.chat.completions.create(
    model="glm-4-flash",
    messages=[{"role": "user", "content": question}]
)
print(f"（耗时 {time.time() - t1:.2f} 秒）")
print(r1.choices[0].message.content or "(无内容)")

print("=" * 50)
print("【Kimi K2.6】")
t2 = time.time()
r2 = kimi_client.chat.completions.create(
    model="kimi-k2.6",
    messages=[{"role": "user", "content": question}]
)
print(f"（耗时 {time.time() - t2:.2f} 秒）")
print(r2.choices[0].message.content or "(无内容)")

# ===== 对比2：Function Calling 决策稳定性 =====
tools = [
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "查询指定城市的天气",
            "parameters": {
                "type": "object",
                "properties": {
                    "city": {"type": "string", "description": "城市名，如杭州、北京"}
                },
                "required": ["city"]
            }
        }
    }
]

fc_question = "杭州今天天气怎么样？"

print("\n" + "=" * 50)
print("【Function Calling 对比】问题：" + fc_question)
print("=" * 50)

for name, client, model in [
    ("智谱 GLM-4-Flash", zhipu_client, "glm-4-flash"),
    ("Kimi K2.6", kimi_client, "kimi-k2.6")
]:
    r = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": fc_question}],
        tools=tools
    )
    msg = r.choices[0].message
    print(f"\n--- {name} ---")
    if msg.tool_calls:
        tc = msg.tool_calls[0]
        print(f"✅ 决定调用工具：{tc.function.name}")
        print(f"   参数：{tc.function.arguments}")
    else:
        print(f"❌ 没调工具，直接回答：{(msg.content or '')[:80]}")
