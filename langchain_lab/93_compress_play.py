import os

# 顶部三件套: 向量模型缓存离线, 智谱联网
os.environ["HF_ENDPOINT"] = "https://hf-mirror.com"
os.environ["HF_HUN_OFFLINE"] = "1"

from dotenv import load_dotenv
load_dotenv()

from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_openai import ChatOpenAI
from langchain_classic.retrievers import ContextualCompressionRetriever
from langchain_classic.retrievers.document_compressors import LLMChainExtractor

脚本目录 = os.path.dirname(os.path.abspath(__file__))
embeddings = HuggingFaceEmbeddings(
    model_name="BAAI/bge-small-zh-v1.5",
    encode_kwargs={"normalize_embeddings": True}
)
db = Chroma(persist_directory=os.path.join(脚本目录, "chroma_db"),
            embedding_function=embeddings)

llm = ChatOpenAI(model="glm-4-flash",
                 api_key=os.getenv("ZHIPU_API_KEY"),
                 base_url="https://open.bigmodel.cn/api/paas/v4",
                 temperature=0.3)

base = db.as_retriever(search_type="similarity", search_kwargs={"k": 3})

compressor = LLMChainExtractor.from_llm(llm)
压缩检索 = ContextualCompressionRetriever(base_compressor=compressor, base_retriever=base)

qs = "加载PDF用的是哪个类?"

print("=== 压缩前: 每块一大段(可能含废话) ===")
原始 = base.invoke(qs)
for d in 原始:
    print(".", d.page_content[:70].replace(chr(10), " "))

print("=== 压缩后: 只保留和问题相关的话 ===")
压缩后 = 压缩检索.invoke(qs)
for d in 压缩后:
    print(".", d.page_content[:100].replace(chr(10), " "))