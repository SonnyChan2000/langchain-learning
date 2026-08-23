# ==== 成绩等级判断 ====
score = int(input("请输入成绩(0-100)"))

if score < 0 or score > 100:
    print("成绩输入错误！")
    exit()
elif score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"成绩是{score}, 等级为{grade}")
