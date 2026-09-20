from langchain_community.document_loaders import WebBaseLoader

url = "https://www.python.org/about/"
loader = WebBaseLoader(url)
docs = loader.load()

print(f"加载了{len(docs)}个文档块")
print("=== 网页正文(前500字) ===")
print(docs[0].page_content[:500])
print("=== 元信息 ===")
print(docs[0].metadata)