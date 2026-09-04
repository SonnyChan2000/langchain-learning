import os
import asyncio
import time
from dotenv import load_dotenv
from openai import AsyncOpenAI

load_dotenv()

zhipu_client = AsyncOpenAI(
    api_key=os.getenv("ZHIPU_API_KEY"),
    base_url="https://open.bigmodel.cn/api/paas/v4"
)

kimi_client = AsyncOpenAI(
    api_key=os.getenv("MOONSHOT_API_KEY"),
    base_url="https://api.moonshot.cn/v1"
)

async def ask_zhipu(question):
    """异步任务1: 问智谱"""
    print("[开始]请求智谱。。。")
    r = await zhipu_client.chat.completions.create(
        model="glm-4-flash",
        messages=[{"role": "user", "content": question}],
    )
    print("[完成] 智谱回答")
    return "GLM :" + (r.choices[0].message.content or "")

async def ask_kimi(question):
    """异步任务2: 问Kimi"""
    print("[开始]请求Kimi")
    r = await kimi_client.chat.completions.create(
        model="kimi-k2.6",
        messages=[{"role": "user", "content": question}],
    )
    print("[完成] Kimi回答")
    return "Kimi :" + (r.choices[0].message.content or "")

async def main():
    question = "用一句话解释什么是api"

    # 同步方式：一个个等
    print("----- 同步调用 -----")
    start = time.time()
    await ask_zhipu(question)
    await ask_kimi(question)
    print(f"同步总耗时：{time.time() - start:.2f}秒\n")

    # 异步方式：同时出发，gather等所有任务完成
    print("----- 异步并发 -----")
    start = time.time()
    results = await asyncio.gather(
        ask_zhipu(question),
        ask_kimi(question)
    )
    print(f"异步总耗时：{time.time() - start:.2f}秒\n")

    for text in results:
        print(text)

asyncio.run(main())
