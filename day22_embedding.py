import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("DASHSCOPE_API_KEY"),
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1")

resp = client.embeddings.create(
    model="text-embedding-v4",
    input="我今天很开心"
)

vector = resp.data[0].embedding
print("向量长度：", len(vector))
print("向量前10个值: ", vector[:10])