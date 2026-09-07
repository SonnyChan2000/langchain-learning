import os
import re
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("ZHIPU_API_KEY"),
    base_url="https://open.bigmodel.cn/api/paas/v4"
)

# ===== 工具实现 =====
fake_data = {
    "杭州": {"weather": "晴", "temp": "28"},
    "北京": {"weather": "小雨", "temp": "22"},
    "上海": {"weather": "多云", "temp": "26"}
}    

def get_weather(city):
    info = fake_data.get(city)
    if info:
        return f"{city}: {info['weather']}, {info['temp']}度"
    return f"没有{city}的天气数据"

def calculate(a, b, op):
    if op == "+": return str(a + b)
    if op == "-": return str(a - b)
    if op == "*": return str(a * b)
    if op == "/": return str(a / b) if b != 0 else "除数不能为0"
    return "不支持的运算符"

# ===== 2.ReAct系统提示词(核心) =====
SYSTEM = """你是一个会使用工具的助手。你必须严格按照以下格式输出：

Thoutht: 你现在的思考(分析需要什么信息、下一步做什么)
Action: 工具名[参数]

可用工具:
- get_weather[城市名]: 查询城市天气
- calculate[数字1, 数字2, 运算符]: 计算器, 运算符为 + - * /之一

每次只能输出一个Thought和一个Action。
当你已经收集到足够信息, 可以回答用户时, 输出：
Thought: 我已经有答案了
Final Answer: 你的最终回答(自然语言)

示例: 
Thought: 用户想知道杭州天气, 我需要查询
Action: get_weather[杭州]
"""

# ===== 3. ReAct 主循环 =====
def run_react(user_question, max_steps=6):
    messages = [
        {"role": "system", "content": SYSTEM},
        {"role": "user", "content": user_question}
    ]

    for step in range(1, max_steps + 1):
        print(f"\n{'='*20} 第{step}轮 {'='*20}")
        r = client.chat.completions.create(
            model="glm-4-flash",
            messages=messages,
            temperature=0.1
        )
        reply = r.choices[0].message.content
        print(reply)
        messages.append({"role": "user", "content": reply})

        # 终止条件：模型给出Final Answer
        if "Final Answer:" in reply:
            print("\n Agent完成")
            return

        match = re.search(r'Action:\s*(\w+)\[(.+?)\]', reply)
        if not match:
            print("\n 没解析出Action, Agent跑偏了")
            return

        tool_name = match.group(1)
        args = match.group(2)

        # 执行工具
        if tool_name == "get_weather":
            result = get_weather(args.strip())
        elif tool_name == "calculate":
            parts = [p.strip() for p in args.split(",")]
            result = calculate(float(parts[0]), float(parts[1]), parts[2])
        else:
            result = f"未知工具：{tool_name}"

        print(f"\n 执行工具{tool_name} → 结果：{result}")

        # 把工具结果以 Observation 喂回去给模型
        messages.append({"role": "user", "content": f"Observation: {result}"})

    print("\n 达到最大轮数")

# ===== 4.测试 =====
run_react("杭州和上海哪个城市温度高? 高多少度")
run_react("帮我计算 3827*941等于多少")


