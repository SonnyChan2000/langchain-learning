import os
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

脚本目录 = os.path.dirname(os.path.abspath(__file__))

embeddings = HuggingFaceEmbeddings(
    model_name="BAAI/bge-small-zh-v1.5",
    encode_kwargs={"normalize_embeddings": True},
)
db = Chroma(
    persist_directory=os.path.join(脚本目录, "chroma_db"),
    embedding_function=embeddings,
)

# 问一个相关问题 vs 一个无关问题, 对比距离
for q in ["文本里怎么加载PDF", "如何修汽车发动机"]:
    带分 = db.similarity_search_with_score(q, k=3)
    print(f"问题: {q}")
    for 块, 分数 in 带分:
        print(f" [距离={分数:.4f}]{块.page_content[:50]}...")
    print()