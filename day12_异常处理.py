# 异常就是程序运行时出现的错误 
# TypeError-把字符串当数字除
# FileNotFoundError-读取不存在的字典键
# KeyError-用了不存在的字典键
# IndexError-列表索引越界
# ValueError-把"abc"转成整数

# try/except:
try:
    num = int(input("请输入一个数字: "))
    print(f"你输入的数字是{num}")
except ValueError:
    print("输入的不是有效数字")

print("程序继续运行")

# 捕获多种异常
try:
    num1 = int(input("请输入被除数:"))
    num2 = int(input("请输入除数:"))
    result = num1/num2
    print(f"结果是{result}")
except ValueError:
    print("请输入有效数字")
except ZeroDivisionError:
    print("除数不能为0")
#合并捕获 用as e拿到具体错误信息
try:
    num1 = int(input("请输入被除数:"))
    num2 = int(input("请输入除数:"))
    result = num1/num2
    print(f"结果是{result}")
except(ValueError, ZeroDivisionError) as e:
    print(f"出错了：{e}")

# else和finally
f = None
try:
    f = open("test.txt", "r", encoding="utf-8")
    content = f.read()
    print(content)
except FileNotFoundError:
    print("文件不存在")
finally:
    if f is not None:
        f.close()
        print("文件已关闭")

# raise抛出异常
def set_age(age):
    if age < 0:
        raise ValueError("年龄不能为负数")
    if age > 150:
        raise ValueError("年龄设置不合理")
    print(f"年龄设置为{age}岁")

try:
    set_age(-5)
except ValueError as e:
    print(f"错误:{e}")

# 自定义异常
class InsufficientBalanceError(Exception):
    """余额不足异常"""
    pass

class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientBalanceError(f"余额不足, 当前余额{self.balance}, 取款{amount}")
        self.balance -= amount
        print(f"取出{amount}元, 剩余{self.balance}元")

account = BankAccount(100)
try:
    account.withdraw(200)
except InsufficientBalanceError as e:
    print(f"操作失败：{e}")

