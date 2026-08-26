# 什么是函数
def print_score(name, score):
    print(f"{name}的成绩是{score}")

print_score("张三", 85)
print_score("李四", 90)

# 定义与调用
def greet():
    print("你好！")
    print("欢迎学习Python")

greet()
greet()

# 执行流程

print("开始")

def say_hello():
    print("Hello")
    print("World")

print("准备调用")
say_hello()
print("结束")

# 举例
def count_len(word):
    print(f"字符长度为：{len(word)}")
#count_len(input("请输入："))


# 函数参数
# 位置参数 按顺序一一对应
def introduce(name, age, city):
    print(f"我叫{name}, 今年{age}岁，来自{city}")

introduce("张三", 25, "杭州")
introduce("李四", 30, "上海")


# 默认参数 设置默认参数 调用时不上传默认 上传覆盖 有默认值参数必须放后面
def greet(name, messeage = "你好"):
    print(f"{name}! {messeage}")

greet("张三")
greet("张三", "早上好")


# 关键字参数
def introduce(name, age, city):
    print(f"我叫{name}, 今年{age}岁, 来自{city}")

introduce(city = "北京", age = 25, name = "张三")
introduce("张三", city = "杭州", age = 25)


# 返回值return
def add(a, b):
    result = a + b
    return result

total = add(3, 9)
print(total)
print(add(2, 4))

def check_age(age):
    if age >= 18:
        return "成年"
    return "未成年"

print(check_age(4))
print(check_age(19))

# return和print区别
def greet_print(name):
    print(f"你好！{name}")

result = greet_print("张三")
print(result)


def greet_print(name):
    return f"你好！{name}"

result = greet_print("张三")
print(result)

# return可以返回多个值
def calculate(a, b):
    return a + b, a - b, a * b

add_result, sub_result, mul_result = calculate(10, 4)
print(add_result)
print(sub_result)
print(mul_result)


# 变量作用域 变量在哪里定义，决定了在哪里能用
# 局部变量 函数内部变量 只在函数内部使用
def test():
    x = 10 
    print(x)

test()


# 全局变量 函数外部变量 整个文件都能读到
x = 20

def test():
    print(x)

test()
print(x)

# 函数内给外部变量赋值无效

x = 12

def test():
    x = 20
    print(x)

test()
print(x)

# 函数内对外部变量操作需要加global
x = 12

def test():
    global x
    x = 20
    print(x)

test()
print(x)







