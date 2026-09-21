import os
os.environ["HF_ENDPOINT"] = "https://hf-mirror.com"
os.environ["HF_HUB_OFFLINE"] = "1"  
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

脚本目录 = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(脚本目录, "text.txt"), encoding="utf-8") as f:
    全文 = f.read()

# 加载→分割
切 = RecursiveCharacterTextSplitter(separators=["\n\n", "\n", "，", "。", " ", ""],
                                   chunk_size=200, chunk_overlap=20)
块们 = 切.split_text(全文)
文档s = [Document(page_content=t) for t in 块们]

# 向量化+存储+检索
embeddings = HuggingFaceEmbeddings(model_name="BAAI/bge-small-zh-v1.5",
                                   encode_kwargs={"normalize_embeddings": True})
db = Chroma.from_documents(文档s, embeddings, persist_directory=os.path.join(脚本目录, "chroma_db"))
retriever = db.as_retriever(search_type="similarity", search_kwargs={"k":3})

# 生成模型: 你在BIGMODEL平台申请过key的话填进去
llm = ChatOpenAI(model="glm-4-flash",api_key=os.getenv("ZHIPU_API_KEY"), base_url="https://open.bigmodel.cn/api/paas/v4", temperature=0.3)

def format_docs(docs):
    return "\n\n".join(d.page_content for d in docs)

prompt = ChatPromptTemplate.from_template(
    "仅根据下面提供的资料回答用户问题。若资料里没有答案，直接说'根据现有资料无法回答'，不要编造。\n\n"
    "【资料】\n{context}\n\n【问题】{question}"
)

chain = (
    {"context": retriever | format_docs, "question": RunnablePassthrough()}
    | prompt | llm | StrOutputParser()
)

while True:
    q = input("提问(回车退出):")
    if not q:
        break
    print("\n回答:", chain.invoke(q), "\n")
