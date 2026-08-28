# ==== 带异常处理计算器 ====
print("---- 带异常处理计算器 ----")

while True:
    num1 = input("请输入第一个数字(q退出): ")
    if num1 == "q":
        print("程序结束")
        break
    try:
        num1 = float(num1)
    except ValueError:
         print("请输入有效数字：")
         continue

    operator = input("请输入运算符(+、-、*、/): ")
    num2 = input("请输入第二个数字(q退出): ")

    try:
        num2 = float(num2)
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
            result = num1 / num2
            print(f"{num1} / {num2} = {result:.10g}")
        else:
            print("不支持的运算符")
            continue           
    except ValueError:
                print("请输入有效数字")
    except ZeroDivisionError:
            print("除数不能为零")
      

    
    