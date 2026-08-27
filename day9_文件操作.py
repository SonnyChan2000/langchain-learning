# 打开和关闭文件 #"r"只读模式，文件不存在的话报错 "w"写入，覆盖原文件内容，原文件不存在则创建 "a"追加，在原文件上增加内容
f = open("test.txt", "w", encoding="utf-8")
f.write("你好, python")
f.close()

with open("test.txt", "w", encoding="utf-8") as f:
    f.write("你好, python")

# 写入文件
# "w"覆盖写入 原内容清空
with open("hello.txt", "w", encoding="utf-8") as f:
    f.write("第一行\n")
    f.write("第二行\n")

# "a"追加写入 末尾添加不清空
with open("hello.txt", "a", encoding="utf") as f:
    f.write("追加的第三行\n")

# 写入多行
lines = ["张三\n", "李四\n", "王五\n"]
with open("names.txt", "w", encoding="utf-8") as f:
    f.writelines(lines)

# 读取文件
# read 一次读全部 返回一个字符串
with open("hello.txt", "r", encoding="utf-8") as f:
    content = f.read()
    print(content)

# readline() 一次读一行
with open("hello.txt", "r", encoding="utf-8") as f:
    line = f.readline()
    print(line)

# 读所有行 返回列表 带\n
with open("hello.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
    print(lines)

# for line in f 逐行遍历
with open("hello.txt", "r", encoding="utf-8") as f:
    for line in f:
        print(line.strip())


# csv文件
# 写入csv文件
import csv

with open("students.csv", "w", encoding="utf-8",newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["姓名", "成绩"])
    writer.writerows([
        ["张三", 85],
        ["李四", 92],
        ["王五", 78]
    ])

# 读取csv
with open("students.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

# os模块
import os

# 查看当前工作目录
print(os.getcwd())

# 拼接路径
path = os.path.join("data","info.txt")
print(path)

# 检查文件是否存在
print(os.path.exists("test.txt"))

# 列出当前目录下所有文件
print(os.listdir("."))