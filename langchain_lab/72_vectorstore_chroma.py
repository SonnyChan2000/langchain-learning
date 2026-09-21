import os
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

脚本目录 = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(脚本目录, "text.txt"), encoding="utf-8") as f:
    全文 = f.read()

切 = RecursiveCharacterTextSplitter(
    separators=["\n\n", "\n", "，", "。", " ", ""],
    chunk_size=200, chunk_overlap=20,
)
块们 = 切.split_text(全文)

文档s = [Document(page_content=t, metadata={"chunk_id": i}) for i,t in enumerate(块们)]

embeddings = HuggingFaceEmbeddings(
    model_name="BAAI/bge-small-zh-v1.5",
    encode_kwargs={"normalize_embeddings": True},
)

db = Chroma.from_documents(
    documents=文档s,
    embedding=embeddings,
    persist_directory=os.path.join(脚本目录, "chroma_db"),
)

print(f"已存入{db._collection.count()}个向量块\n")

while True:
    q = input("输入问题(直接回车退出):")
    if not q:
        break
    结果 = db.similarity_search(q, k=3)
    print(f"——命中{len(结果)}块 ——")
    for i, 块 in enumerate(结果):
        print(f"[{i + 1}](chunk{块.metadata['chunk_id']}){块.page_content[:80]}")
    print()