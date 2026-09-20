import os
from langchain_community.document_loaders import CSVLoader

脚本目录 = os.path.dirname(os.path.abspath(__file__))
loader = CSVLoader(os.path.join(脚本目录, "products.csv"), encoding="utf-8")

docs = loader.load()
print(f"共加载了{len(docs)}行")
for i, doc in enumerate(docs):
    print(f"--- 第{i + 1}行 ---")
    print(doc.page_content)
    print("元信息:", doc.metadata)