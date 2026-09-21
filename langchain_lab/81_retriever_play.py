import os
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

脚本目录 = os.path.dirname(os.path.abspath(__file__))
embeddings = HuggingFaceEmbeddings(
    model_name="BAAI/bge-small-zh-v1.5",
    encode_kwargs={"normalize_embeddings": True}
)
db = Chroma(persist_directory=os.path.join(脚本目录, "chroma_db"),
            embedding_function=embeddings)

retriever = db.as_retriever(search_type="similarity", search_kwargs={"k": 3})
结果 = retriever.invoke("文本里怎么加载PDF")
print(f"返回了{len(结果)}个Document: ")
for i, d in enumerate(结果):
    print(f"[{i + 1}]{d.page_content[:60]}...")
