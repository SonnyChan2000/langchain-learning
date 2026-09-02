import os
import json
from datetime import datetime
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("ZHIPU_API_KEY"),
    base_url="https://open.bigmodel.cn/api/paas/v4/"
)

# 工具1：天气
def get_weather(city):
    fake_data = {
        "杭州": {"weather": "晴", "temp": "28"},
        "北京": {"weather": "小雨", "temp": "22"},
        "上海": {"weather": "多云", "temp": "26"},
    }
    return fake_data.get(city, {"weather": "未知", "temp": "未知"})

# 工具2：计算器
def calculate(a, b, operator):
    if operator == "+": return a + b
    if operator == "-": return a - b
    if operator == "*": return a * b
    if operator == "/": return a / b if b != 0 else "错误: 除数不能为0"
    return "不支持的运算符"

# 工具3：当前时间
def get_current_time():
    now = datetime.now()
    weekdays = ["周一", "周二", "周三", "周四", "周五", "周六", "周日"]
    return {
        "date": now.strftime("%Y-%m-%d"),
        "time": now.strftime("%H:%M"),
        "weekday": weekdays[now.weekday()]
    }

tools = [
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "查询指定城市的实时天气情况",
            "parameters": {
                "type": "object",
                "properties": {
                    "city": {"type": "string", "description": "城市名称, 例如: 杭州、北京、上海"}
                },
                "required": ["city"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "calculate",
            "description": "计算两个数字的加减乘除。当用户需要数学计算时使用",
            "parameters": {
                "type": "object",
                "properties": {
                    "a": {"type": "number", "description": "第一个数字"},
                    "b": {"type": "number", "description": "第二个数字"},
                    "operator": {"type": "string", "enum": ["+", "-", "*", "/"], "description": "运算符"}
                },
                "required": ["a", "b", "operator"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_current_time",
            "description": "获取当前的日期、时间和星期几。当用户问现在几点、今天几号、星期几时使用",
            "parameters": {
                "type": "object",
                "properties":{}
            }
        }
    }
]

# 函数名-真实函数的映射表
available_functions = {
    "get_weather": get_weather,
    "calculate": calculate,
    "get_current_time": get_current_time
}

messages = [
    {"role": "system", "content": "你是一个智能助手, 可以查询天气、进行数学计算、查询时间、需要实时数据或精确计算时必须调用对应工具, 禁止凭空编造"}
]

print("="*40)
print("智能助手已启动!")
print("输入clear清空对话历史, 输入退出结束")
print("="*40)

# 外层循环: 多轮对话
while True:
    user_input = input("\n你: ").strip()

    if user_input in ["退出", "exit", "quit"]:
        print("再见!")
        break
    if user_input == "clear":
        messages = messages[0] #只保留system设定
        print("[系统]对话历史已清空")
        continue
    if not user_input:
        continue

    messages.append({"role": "user", "content": user_input})

    # 内层循环: 工具调用(Day17 的 Agent 骨架)
    while True:
        response = client.chat.completions.create(
            model="glm-4-flash",
            messages=messages,
            tools=tools
        )
        msg = response.choices[0].message

        if not msg.tool_calls:
            print("AI: ", end="", flush=True)
            stream = client.chat.completions.create(
                model="glm-4-flash",
                messages=messages,
                tools=tools,
                stream=True
            )
            full_answer = ""
            for chunk in stream:
                delta = chunk.choices[0].delta.content
                if delta:
                    print(delta, end="", flush=True)
                    full_answer += delta
            print()
            messages.append({"role": "assistant", "content": full_answer})
            break

        for tool_call in msg.tool_calls:
            func_name = tool_call.function.name
            func_args = json.loads(tool_call.function.arguments)

            print(f"[系统]正在调用{func_name}, 参数{func_args}···")

            func_result = available_functions[func_name](**func_args)
            print(f"[系统]{func_name}返回:{func_result}")

            messages.append({
                "role": "tool",
                "tool_call_id": tool_call.id,
                "content": json.dumps(func_result, ensure_ascii=False)
            })