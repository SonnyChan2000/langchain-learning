# ===== 4种基本数据类型 =====
age = 25
price = 19.99
name = "Sonny" 
is_learning = True

print(age)
print(price)
print(name)
print(is_learning)

print(type(age))
print(type(price))
print(type(name))
print(type(is_learning))

# ==== 练习2：字符串操作 ====
first_name = "Sonny"
age = 25
city = "杭州"

#字符串拼接
intro = "我叫" + first_name + ",在" + city
print(intro)

# f-string(推荐写法)
intro2 = f"我叫{first_name},今年{age}岁，在{city}"
print(intro2)

#字符串长度
print(len(first_name))

#转大写/小写
print(first_name.upper())
print(first_name.lower())

#算数运算
a = 17
b = 5

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)


# ==== 练习4：类型转换 ====
# 字符串→整数
num_str = "100"
num_int = int(num_str)
print(num_int + 50) # 150

# 整数→字符串
age = 25
age_str = str(age)
print("我今年" + age_str + "岁")

# 浮点数→整数（注意截断！）
print(int(3.99)) #输出3 不是4!
print(int(9.1))  #输出9

# input输入(运行后在终端输入内容，回车确认)
name = input("请输入你的名字：")
print(f"你好，{name}!")

age_input = input("请输入你的年龄：")
print(f"你输入的是：{age_input}, 类型是：{type(age_input)}")

#创建整数变量并打印类型
height = 172
weight = 67.5
year = 2026

print(height)
print(weight)
print(year)

print(type(height))
print(type(weight))
print(type(year))


# ====创建3个字符串变量，练习拼接和len() ====
name = "Sonny"
age = "25"
hobby = "音乐"

print(f"我叫{name},今年{age}岁,喜欢{hobby}")

print(len(name))
print(len(age))
print(len(hobby))


# ====创建3个浮点数，做一些运算====
price = 19.99
pi = 3.1415
height = 1.72

print(price)
print(type(price))

print(price*3)


# ==== 布尔值，布尔值其实是数字 ====

is_stomachache = True
is_tired = True
has_job = False

print(is_stomachache)
print(type(is_tired))
print(has_job)

print(True - False)
print(True + True)



# ==== 变量赋值与交换 ====
x = 20
y = 10

print(f"交换前: x = {x}, y = {y}")

x , y = y , x

print(f"交换后: x = {x}, y = {y}")


# ==== 个人档案小程序 ====

name = input("请输入你的名字：")
age  = input("请输入你的年龄：")
city = input("请输入你的城市：")
height = input("请输入你的身高：")
is_learning_ai = True

print("=" * 30)
print("个人档案")
print("=" * 30)
print(f"姓名：{name}")
print(f"年龄：{age}")             
print(f"城市：{city}")
print(f"身高：{height}")
print(f"正在学习AI: {is_learning_ai}")
