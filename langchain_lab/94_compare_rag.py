import os,logging
os.environ["HF_ENDPOINT"] = "https://hf-mirror.com"
os.environ["HF_HUB_OFFLINE"] = "1"

from dotenv import load_dotenv
load_dotenv()

from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_openai import ChatOpenAI
from langchain_classic.retrievers.multi_query import MultiQueryRetriever
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough

脚本目录 = os.path.dirname(os.path.abspath(__file__))
embeddings = HuggingFaceEmbeddings(model_name="BAAI/bge-small-zh-v1.5",
                                   encode_kwargs={"normalize_embeddings": True})
db = Chroma(persist_directory=os.path.join(脚本目录, "chroma_db"),
            embedding_function=embeddings)

llm = ChatOpenAI(model="glm-4-flash",
                 api_key=os.getenv("ZHIPU_API_KEY"),
                 base_url="https://open.bigmodel.cn/api/paas/v4",
                 temperature=0.3)

# 两个检索器: 原始similarity vs 优化版 MultiQuery
原始 = db.as_retriever(search_type="similarity", search_kwargs={"k": 3})
优化 = MultiQueryRetriever.from_llm(retriever=db.as_retriever(search_type="similarity", search_kwargs={"k": 2}), llm=llm)

logging.basicConfig()
logging.getLogger("langchain_classic.retriever.multi_query").setLevel(logging.ERROR) # 运行时隐藏MultiQuery细节日志

def format_docs(docs):
    return "\n\n".join(d.page_content for d in docs)

prompt = ChatPromptTemplate.from_template(
    "仅根据下面提供的资料回答用户问题。若资料里没有答案，直接说'根据现有资料无法回答'。\n\n"
    "【资料】\n{context}\n\n【问题】{question}")

def 造链(retriever):
    return ({"context": retriever | format_docs, "question": RunnablePassthrough()}
            | prompt | llm | StrOutputParser())

链原始 = 造链(原始)
链优化 = 造链(优化)

qs = input("输入一个问题试试(例: 文本里怎么加载PDF/加载PDF用的哪个类):")
print("\n【优化前.纯相似度】")
print(链原始.invoke(qs))
print("\n【优化后.Multi-Query多角度】")
print(链优化.invoke(qs))