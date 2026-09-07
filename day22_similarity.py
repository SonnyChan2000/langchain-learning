"""
Day22 第二步: 余弦相似度
用同一个Embedding 接口, 把三句话变成向量, 再算两两相似度。
"""

import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("DASHSCOPE_API_KEY"),
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
)

def get_embedding(text):
    """把一段文字变成向量(一串数字)"""
    resp = client.embeddings.create(
        model="text-embedding-v4",
        input=text,
    )
    return resp.data[0].embedding

def cosine_similarity(vec_a, vec_b):
    """算两个向量的余弦相似度, 返回 0-1 之间的分数"""
    # 点积: 对应位置相乘再累加
    dot = sum(a * b for a, b in zip(vec_a, vec_b))
    # 模长(长度)
    norm_a = sum(a * a for a in vec_a) ** 0.5
    norm_b = sum(b * b for b in vec_b) ** 0.5
    if norm_a == 0 or norm_b == 0:
        return 0.0
    return dot / (norm_a * norm_b)

# 实验: 三句话, 前两句意思接近, 第三句完全不同
texts = [
    "我今天很开心",
    "我今天心情很好",
    "今天下雨了"
]

vecs = [get_embedding(t) for t in texts]

# 两两对个分
pairs = [(0 , 1),(0, 2), (1, 2)]
for i, j in pairs:
    score = cosine_similarity(vecs[i], vecs[j])
    print(f"'{texts[i]}' vs '{texts[j]}' 相似度 = {score:.4f}")