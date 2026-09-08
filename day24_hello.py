"""
Day24 练习1: 最快跑一个Web服务出来
"""
from fastapi import FastAPI

# 创建应用
app = FastAPI()

# 根路径"/"的GET接口
@app.get("/")
def read_root():
    return {"message": "Hello World!"}

@app.get("/hello/{name}")
def say_hello(name: str):
    return {"msg": f"你好, {name}!"}