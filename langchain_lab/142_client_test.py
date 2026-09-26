import requests

url = "http://127.0.0.1:8000/chat"

# 第一条: 算数(测试工具)
r1 = requests.post(url, json={"message": "帮我算5 + 7等于多少", "thread_id": "测试1"})
print("算数:", r1.json())

# 第二条: 查资料(测试RAG工具)
r2 = requests.post(url, json={"message": "用查资料工具查一下: LangChain是什么?", "thread_id": "测试1"})
print("查资料:", r2.json())

# 第三条: 不同会话号, 验证记忆隔离(应该不记得测试1的内容)
r3 = requests.post(url, json={"message": "我刚才问了什么?", "thread_id": "另一个会话"})
print("新会话:", r3.json())    