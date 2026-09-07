"""
Day23 综合项目: 完整RAG文档问答工具
读取 knowledge.txt - 切段落 - 建索引 - 检索 - 塞进prompt - 大模型作答
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
    resp = client.embeddings.create(model="text-embedding-v4", input=text)
    return resp.data[0].embedding

def cosine_similarity(vec_a, vec_b):
    dot = sum(a * b for a, b in zip(vec_a, vec_b))
    norm_a = sum(a * a for a in vec_a) ** 0.5
    norm_b = sum(b * b for b in vec_b) ** 0.5
    if norm_a == 0 or norm_b == 0:
        return 0.0
    return dot / (norm_a * norm_b)

# 加载+建索引：读文件、按空行切段、向量化
with open("knowledge.txt", encoding="utf-8") as f:
    raw = f.read()
# 按空行切段, 并去掉首尾空白
docs = [sec.strip() for sec in raw.split("\n\n") if sec.strip()]

print(f"读入{len(docs)}段文档, 开始建索引。。。")
index = [(doc, get_embedding(doc)) for doc in docs]
print("索引建立完成\n")

# 检索：查询向量化-算相似度-取top3
query = "embedding和prompt engineering有什么关系"
q_vec = get_embedding(query)

scored = [(cosine_similarity(q_vec, vec), doc) for doc, vec in index]
scored.sort(reverse=True)
top_chunks = [doc for _, doc in scored[:3]]

print("检索到最相关的3段: ")
for i, c in enumerate(top_chunks, 1):
    print(f"{i}.{c[:30]}...")
print()

system_prompt = f"""
你是资料库问答助手。请只根据以下资料回答：

资料:
1. {top_chunks[0]}
2. {top_chunks[1]}
3. {top_chunks[2]}

要求: 只依据以上资料回答, 资料里没有的内容, 就说"资料里没有", 不要编造。
"""

# 对话块: 调大模型生成回答
messages = [
    {"role": "system", "content": system_prompt},
    {"role": "user", "content": query},
]

resp = client.chat.completions.create(
    model = "qwen-turbo",
    messages=messages,
)

print("=="*20)
print("模型回答:")
print(resp.choices[0].message.content)