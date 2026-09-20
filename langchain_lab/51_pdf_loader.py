import os
from langchain_community.document_loaders import PyPDFLoader

脚本目录 = os.path.dirname(os.path.abspath(__file__))

pdf路径 = os.path.join(脚本目录, "test.pdf")

loader = PyPDFLoader(pdf路径)
docs = loader.load()

print(f"共加载了{len(docs)}页")
print("=== 第一页内容(前300字) ===")
print(docs[0].page_content[:300])
print("=== 第1页元信息 ===")
print(docs[0].metadata)