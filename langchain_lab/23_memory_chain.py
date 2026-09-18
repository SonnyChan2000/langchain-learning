import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage

load_dotenv()

llm = ChatOpenAI(
    api_key=os.getenv("ZHIPU_API_KEY"),
    model="glm-4-flash",
    base_url="https://open.bigmodel.cn/api/paas/v4/",
)

prompt = ChatPromptTemplate.from_messages([
    ("system", "你是陪伴式助手, 记住对话内容, 语气自然。"),
    MessagesPlaceholder(variable_name="history"),
    ("human", "{input}"),
])

history = []

print("对话开始(输入exit退出)\n")
while True:
    user_input = input("你: ")
    if user_input ==  "exit":
        break

    chain = prompt | llm
    response = chain.invoke({"history": history, "input": user_input})
    ai_text = response.content
    print(f"AI: {ai_text}\n")

    history.append(HumanMessage(content=user_input))
    history.append(AIMessage(content=ai_text))
