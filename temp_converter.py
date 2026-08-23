# ==== 温度转换器 ====
print("---- 温度转换器 ----")
print("1. 摄氏 → 华氏")
print("2. 华氏 → 摄氏")

choice = input("请选择(1或2):")
temp = float(input("请输入温度值："))

if choice == "1":
    result = temp * 9 / 5 + 32
    print(f"{temp}℃ = {result}℉")
elif choice == "2":
    result = (temp - 32) * 5 / 9
    print(f"{temp}℉ = {result}℃")
else:
    print("输入错误，请重新输入")

