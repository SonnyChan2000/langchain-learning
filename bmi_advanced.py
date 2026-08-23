# ==== BMI等级判断进阶版 ====
height = float(input("请输入你的身高(米):"))
weight = float(input("请输入你的体重(公斤):"))

if height <= 0 or weight <= 0:
    print("输入有误！身高体重必须大于0")
else:
    bmi = weight / (height ** 2)
    print(f"你的BMI是{bmi:.1f}")

    if bmi < 18.5:
        category = "偏瘦"
        advice = "多吃点好的"
    elif bmi < 24:
        category = "正常"
        advice = "保持住！"
    elif bmi < 28:
        category = "偏胖"
        advice = "注意锻炼"
    else:
        category = "肥胖"
        advice = "建议咨询医生"
    print(f"分类：{category}, 建议：{advice}")
