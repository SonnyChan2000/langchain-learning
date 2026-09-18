import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate

load_dotenv()

llm = ChatOpenAI(
    api_key=os.getenv("ZHIPU_API_KEY"),
    model="glm-4-flash",
    base_url="https://open.bigmodel.cn/api/paas/v4",
)

template = PromptTemplate.from_template(
    "你是{角色}。请用{语气}的语气, 帮客户解答：{问题}"
)

p = template.invoke({
    "角色": "淘宝售后客服",
    "语气": "热情耐心",
    "问题": "我想退耳机, 怎么操作？"
})

print("===== 生成的提示词 =====")
print(p.text)