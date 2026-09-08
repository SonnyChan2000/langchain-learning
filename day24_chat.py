"""
Day24 练习3: 把大模型聊天包成Web API
POST/chat - 收JSON{"messages": "..."} - 调大模型 - 返回回复
"""

import os
from fastapi import FastAPI
from pydantic import BaseModel
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("DASHSCOPE_API_KEY"),
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
)

app = FastAPI()

# 定义请求体结构: 客户端POST上来的数据长什么样
class ChatRequest(BaseModel):
    message: str        

# 对话接口
@app.post("/chat")
def chat(req: ChatRequest):
    resp = client.chat.completions.create(
        model="qwen-turbo",
        messages=[{"role": "user", "content": req.message}],
    )
    return {"reply": resp.choices[0].message.content}