# ==== 判断某年某月有多少天 ====
# 第一步：输入年份和月份
# 第二步：判断月份合法性(1-12), 不合法直接提示
# 第三步：判断天数 月份为1,3,5,7,8,10,12时天数为31 月份为4,6,9,11时天数为30 月份为2时先判断是否为闰年 闰年天数29 平年天数28

year = int(input("请输入年份："))
month = int(input("请输入月份："))

if month <= 0 or month > 12:
    print("月份输入有误，请重新输入")
else:
    if month in [1,3,5,7,8,10,12]:
        days = 31
    elif month in [4,6,9,11]:
        days = 30
    else:
        if (year % 4 == 0 and  year % 100 != 0) or year % 400 == 0:
            days = 29
        else:
            days = 28
    print(f"{year}年{month}月有{days}天")
