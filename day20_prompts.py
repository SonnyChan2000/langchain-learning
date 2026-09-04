import os
import json
import re
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("ZHIPU_API_KEY"),
    base_url="https://open.bigmodel.cn/api/paas/v4"
)

def ask(system, user, model="glm-4-flash"):
    r = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": system},
            {"role": "user", "content": user}
        ]
    )
    return r.choices[0].message.content

code = """
def calc_average(numbers):
    total = 0
    for n in numbers:
        total = total + n
    avg = total / len(numbers)
    print(avg)
"""
# 裸问：没有角色
bad = ask(
    system="你是一个助手",
    user=f"看看这段代码：\n{code}"
)
# 角色设定：资深工程师视角
good = ask(
    system="你是一位有10年经验的Python高级工程师, 正在做Code Review。"
           "请从三个维度审查代码: 1.潜在bug(如空列表会怎样) 2.Pthonic写法 3.边界情况。每个问题给出具体修改建议。",
    user=f"请审查以下代码：\n{code}"
)

print("===== 无角色设定 =====\n", bad)
print("===== 资深工程师角色 =====\n", good)

# ===== 实验2：输出格式控制(结构化JSON) =====
review = "这家店的牛肉面太好吃了, 肉给的很足, 就是排队等了40分钟, 服务员态度一般。"

# 只说"分析评论"
bad2 = ask(
    system="你是一个助手。",
    user=f"分析这条评论：{review}"
)
# 明确JSON格式 + 字段说明
good2 = ask(
    system="你是一个评论分析器。必须只输出JSON, 不要输出任何其他文字。",
    user=f"""分析以下评论,输出JSON, 包含字段：
    -sentiment: 情感倾向, 只能是positive/negative/neutral
    -rating: 总体评分1-5的整数
    -keywords: 关键词数组, 不超过5个
    -summary: 一句话总结, 30字以内
评论：{review}"""
)
match = re.search(r'\{.*\}', good2, re.DOTALL)
data = json.loads(match.group())

print("===== 自由格式 =====\n", bad2)
print("\n===== JSON 格式 =====\n", good2)
print(type(data))

# ===== 实验3：Few-shot示例(客服问题分类) =====

# Zero-shot：只说分类要求，不给例子
bad3 = ask(
    system="你是客服分类器。把问题分为：账单、技术、咨询、投诉。",
    user="我的套餐这个月怎么多扣了20块?"
)

# Few-shot: 给3个例子示范分类标准
good3 = ask(
    system="你是客服分类器。只输出类别名称。只输出类别本身(账单/技术/咨询/投诉其中一个), 禁止加'问题'等任何额外字",
    user="""请将用户问题分类。
    
    示例:
    问题: wifi连不上怎么办
    类别: 技术
    
    问题: 你们的营业时间是几点
    类别: 咨询
    
    问题: 我要找你们领导, 太过分了
    类别: 投诉
    
    现在请分类:
    问题: 我的套餐这个月怎么多扣了20块?
    类别: """
)

print("===== Zero-shot(无示例) =====\n", bad3)
print("===== Few-shot(有示例) =====\n", good3)

# ===== 实验4: COT思维链(推理题) =====
question = "一个水池, 进水管A单独注满要6小时, 出水管B单独排空要8小时。两管同时开, 几小时注满?"

bad4 = ask(
    system="你是一个助手。",
    user=f"{question} 请直接给出答案。"
)

# COT: 要求分步推理
good4 = ask(
    system="你是一个数学老师。",
    user=f"{question}\n请一步步思考: 先列出已知条件, 再计算每小时净进水量, 最后求时间。"
)

print("===== 直接回答 =====\n", bad4)
print("===== 思维链 =====\n", good4)