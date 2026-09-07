"""
Day22第三步: 语义搜索(embedding检索)
把5条文档建成"索引",输入一句查询, 按语义相似度排出最相关的文档。
"""
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("DASHSCOPE_API_KEY"),
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
)

def get_embedding(text):
    resp = client.embeddings.create(model="text-embedding-v4", input=text)
    return resp.data[0].embedding

def cosine_similarity(vec_a, vec_b):
    dot = sum(a * b for a, b in zip(vec_a, vec_b))
    norm_a = sum(a * a for a in vec_a) ** 0.5
    norm_b = sum(b * b for b in vec_b) ** 0.5
    if norm_a == 0 or norm_b == 0:
        return 0.0
    return dot / (norm_a * norm_b)

# 1.知识库: 5条"简历库"文档
docs = [
    "精通Python数据分析, 熟练使用pandas、numpy、matplotlib做数据清洗与可视化",
    "有两年智能制造经验, 用Python写了自动化测试脚本, 减少人工操作",
    "熟悉神经网络基础, 会用PyTorch训练并调优图像分类模型",
    "掌握Langchain与智能体开发, 能搭建带工具调用和记忆的AI Agent应用",
    "有Web后端经验, 了解FastAPI、REST API的搭建与部署",
]
# 2.建索引: 把每条文档全都向量化, 存成(原文, 向量)列表
index = [(doc, get_embedding(doc)) for doc in docs]
print("已把5条文档建好索引")

# 3.用户查询, 同样向量化
query = "我想找一份AI智能体开发相关的工作"
query_vec = get_embedding(query)

# 4.查询向量和每条文档向量 算相似度
scored = []
for doc ,vec in index:
    score = cosine_similarity(query_vec, vec)
    scored.append((score, doc))

# 5.按分数从高到低排序, 取前3
scored.sort(reverse=True)
print(f"\n查询: {query}\n " + "="*50)
for score, doc in scored[:3]:
    print(f"相似度{score:.4f}|{doc}")