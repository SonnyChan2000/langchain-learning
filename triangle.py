# ==== 判断三角形类型 ====
a = float(input("请输入第一条边："))
b = float(input("请输入第二条边："))
c = float(input("请输入第三条边："))

if a + b > c and b + c > a and c + a > b:
    if a == b == c:
        print("等边三角形")
    elif a == b or b == c or c == a:
        print("等腰三角形")
    else:
        print("普通三角形")
else:
    print("不能构成三角形")
    