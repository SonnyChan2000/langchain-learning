import os
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

脚本目录 = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(脚本目录, "text.txt"), encoding="utf-8") as f:
    全文 = f.read()

切 = RecursiveCharacterTextSplitter(
    separators=["\n\n", "\n", "，", "。", " ", ""],
    chunk_size=200, chunk_overlap=20,
)
块们 = 切.split_text(全文)
文档s = [Document(page_content=t) for t in 块们]

embeddings = HuggingFaceEmbeddings(
    model_name="BAAI/bge-small-zh-v1.5",
    encode_kwargs={"normalize_embeddings": True},
)

db = FAISS.from_documents(文档s, embeddings)
db.save_local(os.path.join(脚本目录,  "faiss_index"))

db2 = FAISS.load_local(
    os.path.join(脚本目录, "faiss_index"),
    embeddings,
    allow_dangerous_deserialization=True,
)

q = "这段文字主要在讲什么"
结果 = db2.similarity_search(q, k=3)
print(f"FAISS命中{len(结果)}块")
for i,块 in enumerate(结果):
    print(f"[{i + 1}]{块.page_content[:60]}...")