import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("ZHIPU_API_KEY"),
    base_url="https://open.bigmodel.cn/api/paas/v4/"
)

question = "给奶茶店起3个名字"

for temp in[0.0, 0.9]:
    print(f"\n===== temperature={temp} =====")
    response = client.chat.completions.create(
        model="glm-4-flash",
        messages=[{"role": "user", "content":question}],
        temperature = temp
    )
    print(response.choices[0].message.content)
