import math
from langchain_huggingface import HuggingFaceEmbeddings

embeddings = HuggingFaceEmbeddings(
    model_name="BAAI/bge-small-zh-v1.5",
    encode_kwargs={"normalize_embeddings": True},
)

# 3个句子, 前两个意思相近, 第三个无关
a = "我喜欢猫"
b = "我超爱猫咪"
c = "今天股票涨了不少"

def 余弦(v1, v2):
    return sum(x * y for x, y in zip(v1, v2))

va, vb, vc = (
    embeddings.embed_query(a),
    embeddings.embed_query(b),
    embeddings.embed_query(c),
)

print(f"向量维度: {len(va)}")
print(f"前5个数字: {va[:5]}")
print(f" A-B相似度: {余弦(va, vb):.4f}")
print(f" A-C相似度: {余弦(va, vc):.4f}")
print(f" B-C相似度: {余弦(vb, vc):.4f}")