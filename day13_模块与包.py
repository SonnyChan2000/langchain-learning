# import 3种写法
# 导入整个模块
import math
print(math.sqrt(16))

# 导入模块中的功能
from math import sqrt, pi
print(sqrt(16))
print(pi)

# 给模块起别名 模块名太长时使用
import math as m
print(m.sqrt(16))

# 常用标准库
# math 数学计算
import math

print(math.sqrt(16)) # 平方根
print(math.ceil(4.2)) # 向上取整
print(math.floor(4.7)) # 向下取整
print(math.pow(2, 3)) # 幂运算
print(math.factorial(5)) # 阶乘
print(math.pi)

# random 随机数
import random

print(random.randint(1, 100)) # 1到100随机整数
print(random.random())        # 0-1之间随机小数
print(random.choice(["苹果", "香蕉", "梨子"])) # 随机选一个

fruits = ["苹果", "香蕉", "橘子", "葡萄"]
random.shuffle(fruits)
print(fruits)

# datetime 日期时间
from datetime import datetime, timedelta

now = datetime.now()
print(now)
print(now.year)
print(now.month)
print(now.strftime("%Y年%m月%d日"))

tomorrow = now + timedelta(days=1)
print(tomorrow)

# os 操作系统接口
import os

print(os.getcwd())
print(os.listdir("."))
print(os.path.exists("test.txt"))
print(os.path.join("folder","a.txt"))

# pip安装第三方包 自己写模块
import requests

response = requests.get("https://www.baidu.com")
print(response.status_code)
print(len(response.text))