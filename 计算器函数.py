# 写四个函数 实现加减乘除
def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiple(a, b):
    return a * b
def divide(a, b):
    if b == 0:
        return "错误! 除数不能为0"
    return round(a / b, 1)

print(add(10, 3))
print(subtract(10, 3))
print(multiple(10, 3))
print(divide(10, 3))
print(divide(10, 0))
    
