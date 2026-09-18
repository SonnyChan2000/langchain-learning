import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser

load_dotenv()

llm = ChatOpenAI(
    api_key=os.getenv("ZHIPU_API_KEY"),
    model="glm-4-flash",
    base_url="https://open.bigmodel.cn/api/paas/v4/",
)

parser = JsonOutputParser()

prompt = ChatPromptTemplate([
    ("system", "你是一个商品信息提取器。只输出JSON, 不要输出其它任何文字。\nJSON格式: {{\"name\": \"商品名\", \"price\": 价格数字, \"category\": \"分类\"}}"),
    ("user", "帮我提取: '无线降噪耳机, 打折后299元, 属于数码配件'")
])

chain = prompt | llm | parser

result = chain.invoke({})
print("解析结果: ", result)
print("类型: ", type(result))
print("取价格字段: " , result["price"])