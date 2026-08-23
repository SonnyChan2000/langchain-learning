# ==== 简易成绩分析系统 ====
# 找出最高分和最低分(谁得的)
# 计算平均分
# 输出类似：
# 最高分：小明 95分
# 最低分：小红 72分
# 平均分：83.7分

name1 = input("请输入第一名学生的姓名：")
score1 = float(input("请输入第一名学生的成绩："))
name2 = input("请输入第二名学生的姓名：")
score2 = float(input("请输入第二名学生的成绩："))
name3 = input("请输入第三名学生的姓名：")
score3 = float(input("请输入第三名学生的成绩："))

score_average = (score1 + score2 + score3) / 3

if score1 >= score2 and score1 >= score3:
    if score2 >= score3:
        print(f"最高分：{name1} {score1}分")
        print(f"最低分：{name3} {score3}分")
        print(f"平均分：{score_average}分")
    else:
        print(f"最高分：{name1} {score1}分")
        print(f"最低分：{name2} {score2}分")
        print(f"平均分：{score_average}分")
elif score2 >= score1 and score2 >= score3:
    if score1 >= score3:
        print(f"最高分：{name2} {score2}分")
        print(f"最低分：{name3} {score3}分")
        print(f"平均分：{score_average}分")
    else:
        print(f"最高分：{name2} {score2}分")
        print(f"最低分：{name1} {score1}分")
        print(f"平均分：{score_average}分")
else:
    if score1 >= score2:
        print(f"最高分：{name3} {score3}分")
        print(f"最低分：{name2} {score2}分")
        print(f"平均分：{score_average}分")
    else:
        print(f"最高分：{name3} {score3}分")
        print(f"最低分：{name1} {score1}分")
        print(f"平均分：{score_average}分")
