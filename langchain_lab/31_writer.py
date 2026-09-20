import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

llm = ChatOpenAI(
    api_key=os.getenv("ZHIPU_API_KEY"),
    model="glm-4-flash",
    base_url="https://open.bigmodel.cn/api/paas/v4"
)

大纲_prompt = ChatPromptTemplate.from_messages([
    ("system", "你是资深编辑, 根据主题先生成文章大纲。只输出大纲, 把文章分成角色清晰的章节, 每行一个章节标题, 行首用'1'、'2'...编号, 每节一句说明, 不超过5节"),
    ("user", "主题: {主题}"),
])
大纲_chain = 大纲_prompt | llm

扩写_prompt = ChatPromptTemplate.from_messages([
    ("system", "你是写手, 根据大纲把用户指定的那一节扩写成300字左右的正文, 语言通俗。"),
    ("user", "文章大纲: \n{大纲}\n\n请扩写这一节: {章节}"),
])
扩写_chain = 扩写_prompt | llm

主题 = "如何用Langchain做RAG问答系统"

大纲文本 = 大纲_chain.invoke({"主题": 主题}).content
print("【大纲】\n", 大纲文本, "\n")

import re
章节们 = [行.strip() for 行 in 大纲文本.split("\n") if len(行.strip()) > 3]
print("【拆分出的章节数】", len(章节们))
文章 = []

for i, 章 in enumerate(章节们, 1):
    正文 = 扩写_chain.invoke({"大纲": 大纲文本, "章节": 章}).content
    文章.append(f"##{章}\n{正文}")
    print(f"[{i}/{len(章节们)}] 已扩写: {章[:25]}...")

print("\n【扩写完成, 共", len(文章) ,"节】")

润色_prompt = ChatPromptTemplate([
    ("system", "你是主编, 把下面的文章润色成通顺流畅、逻辑连贯的完整文章, 保持原有分节结构, 删除重复内容。"),
    ("user", "原文: \n{草稿}"),
])
润色_chain = 润色_prompt | llm

全文草稿 = "\n\n".join(文章)
print("\n【润色中...】")
润色结果 = 润色_chain.invoke({"草稿": 全文草稿}).content
print("【润色后全文】\n", 润色结果)

输出路径 = os.path.join(os.path.dirname(os.path.abspath(__file__)), "文章_" + 主题.replace(" ","_") + ".md")
with open(输出路径, "w", encoding="utf-8") as f:
    f.write("# " + 主题 + "\n\n")
    f.write(润色结果)
    f.write("\n\n---\n> 由多步骤写作助手生成(glm-4-flash)\n")
print(f"\n 文章已保存到: {输出路径}")









