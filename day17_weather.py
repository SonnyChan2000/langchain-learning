import os
import json
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("ZHIPU_API_KEY"),
    base_url="https://open.bigmodel.cn/api/paas/v4/"
)

# 1.真实函数(用假数据模拟天气)
def get_weather(city):
    fake_data = {
        "杭州": {"weather": "晴", "temp": "28"},
        "北京": {"weather": "小雨", "temp": "22"},
        "上海": {"weather": "多云", "temp": "26"},
    }
    return fake_data.get(city, {"weather": "未知", "temp": "未知"})

def calculate(a, b, operator):
    if operator == "+":
        return a + b
    if operator == "-":
        return a - b
    if operator == "*":
        return a * b
    if operator == "/":
        return a / b if b != 0 else "错误: 除数不能为0"
    return "不支持的运算符"

# 2.工具说明书：告诉模型"有这个工具可用"
tools = [
    {"type": "function",
     "function":{
         "name": "get_weather",
         "description": "查询指定城市的实时天气情况",
         "parameters": {
             "type": "object",
             "properties":{
                 "city": {
                     "type": "string",
                     "description": "城市名称, 例如: 杭州、北京、上海"
                 }
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
            "parameters":{
                "type": "object",
                "properties":{
                    "a": {"type": "number", "description": "第一个数字"},
                    "b": {"type": "number", "description": "第二个数字"},
                    "operator": {
                        "type": "string",
                        "enum": ["+", "-", "*", "/"],
                        "description": "运算符"
                    }
                },
                "required": ["a", "b", "operator"]
            }
        }
    }
]



available_functions = {
    "get_weather": get_weather,
    "calculate": calculate
}
messages = [
    {"role": "system", "content": "你是一个智能助手。可以查询天气和进行数学计算, 需要实时数据或精确计算时必须调用对应工具，禁止凭空编造。"},
    {"role": "user", "content": "杭州天气怎么样？"}
]   

while True:
    response = client.chat.completions.create(
        model="glm-4-flash",
        messages=messages,
        tools=tools
    )

    msg = response.choices[0].message

    if not msg.tool_calls:
        print("\nAI:" + msg.content)
        break

    messages.append(msg)

    for tool_call in msg.tool_calls:
            # 1.解析模型要调用的函数名和参数
        func_name = tool_call.function.name
        func_args = json.loads(tool_call.function.arguments)

        print(f"[系统]调用函数{func_name}, 参数{func_args}")
            # 2.真正执行函数
        func_result = available_functions[func_name](**func_args)
        print(f"[系统]函数返回：{func_result}")

            # 3.把结果作为tool 消息加入历史
        messages.append({
            "role": "tool",
            "tool_call_id": tool_call.id,
            "content": json.dumps(func_result, ensure_ascii=False)
        })
        