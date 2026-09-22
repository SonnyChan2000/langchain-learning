import os, logging

# 顶部固定三件套: 向量模型走缓存离线, 但智谱要联网(不设离线)
os.environ["HF_ENDPOINT"] = "https://hf-mirror.com"
os.environ["HF_HUN_OFFLINE"] = "1"

from dotenv import load_dotenv
load_dotenv()

from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_openai import ChatOpenAI
from langchain_classic.retrievers.multi_query import MultiQueryRetriever

脚本目录 = os.path.dirname(os.path.abspath(__file__))
embeddings = HuggingFaceEmbeddings(model_name="BAAI/bge-small-zh-v1.5", encode_kwargs={"normalize_embeddings": True})
db = Chroma(persist_directory=os.path.join(脚本目录, "chroma_db"), embedding_function=embeddings)

# 生成多角度问题的LLM(联网智谱), 从.env里读key
llm = ChatOpenAI(model="glm-4-flash", api_key=os.getenv("ZHIPU_API_KEY"), base_url="https://open.bigmodel.cn/api/paas/v4", temperature=0.3)
base = db.as_retriever(search_type="similarity",search_kwargs={"k": 2})
mq = MultiQueryRetriever.from_llm(retriever=base, llm=llm)

# 打印它生成了哪些角度(INFO日志)
logging.basicConfig()
logging.getLogger("langchain_classic.retrievers.multi_query").setLevel(logging.INFO)


qs = "怎么读取PDF文件?"

结果 = mq.invoke(qs)
print(f"\nMultiQuery最终返回{len(结果)}块(多角度并集去重)")
for i, d in enumerate(结果):
    print(f"[{i + 1}]{d.page_content[:50].replace(chr(10),' ')}")
print("92 脚本目录 =", 脚本目录)
