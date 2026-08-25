# ==== 元组 不可变的列表 ====
fruit_list = ["苹果", "香蕉", "梨子"]
fruit_list[2] = "葡萄" #可修改

fruit_tuple = ("苹果", "香蕉", "梨子") # 不可修改

# 单元组必须加，
t1 = (1,)

# ==== 集合set ====
# 元素不重复 无序(不能用索引)
s = {1, 2, 2, 3, 3, 5,}
print(s)

a = {"张三", "李四", "王五"}
b = {"李四", "王五", "赵六"}
print(a & b)
print(a | b)
print(a - b)

# 空集用set(), {}表示空字典

# ==== 字符串进阶 ====
# split()切分 切分得到的是列表
text = "python is easy"
words = text.split()
print(words)

csv = "张三,25,机械"
info = csv.split(",") #按,切分
print(info)

data = "a-b-c-d-e"
print(data.split("-",2)) #按-切分 切前两个-

# join()合并 把列表拼成字符串 split的反向操作
words = ["python", "is", "easy"]
sentence = " ".join(words)
print(sentence)

csv = ",".join(["张三", "25", "机械"])
print(csv)

# strip() 去首尾空白 处理用户输入时常用
text = " hello world "
print(text.strip())
print(text.lstrip())
print(text.rstrip())

#name = input("请输入你的姓名：").strip()
#print(name)


# replace()替换 字符串本身不可变 需要用新变量接住
text = "我喜欢java"
new_text = text.replace("java", "python")
print(new_text)

text2 = "a-b-c-d"
print(text2.replace("-", "/"))

# 大小写转换
text = "Hello Python"

print(text.upper()) #大写
print(text.lower()) #小写
print(text.title()) #首字母大写

# 判断开头结尾
print(text.startswith("Hello"))
print(text.endswith("java"))

# 查找
print(text.find("Python")) #Python从第6个位置开始 输出6 如果找不到 返回-1
print(text.count("l")) #字母l出现的次数

# 判断内容类型
print("123".isdigit())
print("abc".isalpha())
print("1234a".isdigit())
print("abc1".isalpha())



