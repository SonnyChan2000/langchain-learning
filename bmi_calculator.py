# ==== BMI计算器 ====
print("---- BMI计算器 ----")

height = float(input("请输入你的身高(米):"))
weight = float(input("请输入你的体重(kg):"))
bmi = weight/(height ** 2)


print(f"你的BMI是：{bmi:.1f}")

if   bmi < 18.5:
    print("偏瘦，多吃点")
elif bmi < 24:
    print("正常，保持住")
elif bmi < 28:
    print("偏胖，注意锻炼")
else:
    print("肥胖，建议咨询医生")


