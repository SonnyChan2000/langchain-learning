# ==== 比较运算符 ====
x = 20 
y = 10

print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= 10)
print(x <= 5)


# ==== 逻辑运算符 ====
age = 25
income = 8000
has_house = False

print(f"逻辑运算符输出结果")
print(age > 18 and income > 5000)
print(age > 18 and has_house)
print(age > 18 or has_house)
print(age < 18 or has_house)
print(not age > 18)
print(not has_house)


# ==== 条件判断基础 ====
age = 20 

print("条件判断基础输出结果")
if age >= 18:
    print("你是成年人")
else:
    print("你是未成年人")


# ==== if/elif/else
score = 85

print("if/elif/else输出结果")
if score >= 90:
    print("优秀")
elif score >= 80:
    print("良好")
elif score >= 60:
    print("及格")
else:
    print("不及格")


# ==== 组合使用比较+逻辑+条件判断 ====
age = 25
has_ticket = True

print("组合使用比较+逻辑+条件判断输出结果")
if age > 18 and has_ticket:
    print("可以入场")
elif age > 18 and not has_ticket:
    print("你成年了但没买票，去买票吧")
else:
    print("未成年人不能入场")
