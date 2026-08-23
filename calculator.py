# ==== 简易计算器 ====
print("---- 简易计算器 ----")

num1 = float(input("请输入第一个数字: "))
operator = input("请输入运算符(+、-、*、/): ")
num2 = float(input("请输入第二个数字: "))

if operator == "+" :
    result = num1 + num2
    print(f"{num1} + {num2} = {result:.10g}")
elif operator == "-" :
    result = num1 - num2
    print(f"{num1} - {num2} = {result:.10g}")
elif operator == "*" :
    result = num1 * num2
    print(f"{num1} * {num2} = {result:.10g}")
elif operator == "/" :
    if num2 == 0 :
        print("错误，除数不能为0")
    else:
        result = num1 / num2
        print(f"{num1} / {num2} = {result:.10g}")
else:
    print("不支持的运算符")


    
    