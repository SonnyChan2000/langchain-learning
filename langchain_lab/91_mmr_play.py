import os
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

os.environ["HF_ENDPOINT"] = "https://hf-mirror.com"
os.environ["HF_HUB_OFFLINE"] = "1"

脚本目录 = os.path.dirname(os.path.abspath(__file__))
embeddings = HuggingFaceEmbeddings(model_name="BAAI/bge-small-zh-v1.5",
                                   encode_kwargs={"normalize_embeddings": True})
db = Chroma(persist_directory=os.path.join(脚本目录, "chroma_db"),
            embedding_function=embeddings)

# 纯相似度
sim_retriever = db.as_retriever(search_type="similarity",
                                search_kwargs={"k": 3})
# MMR: k=取3块, fetch_k=先拉10块候选, lambda_mult=多样性权重(0~1, 越小越多样)
mmr_retirever = db.as_retriever(search_type="mmr",
                                search_kwargs={"k": 3, "fetch_k": 10, "lambda_mult": 0.5})


qs = "文本里怎么加载PDF?"
print("=== similarity(纯相似度,可能重复) ===")
for d in sim_retriever.invoke(qs):
    print(".", d.page_content[:45].replace("\n", " "))
print("\n=== mmr(相似 + 多样) ===")
for d in mmr_retirever.invoke(qs):
    print(".", d.page_content[:45].replace("\n", " "))
print("91 脚本目录 =", 脚本目录)