class_a = ["张三", "李四", "王五", "赵六", "李四", "王五"]
class_b = ["李四", "王五", "钱七", "孙八", "钱七"]

set_a = set(class_a)
set_b = set(class_b)

print(set_a & set_b)
print(set_a | set_b)
print(set_a - set_b)
print(len(set_a | set_b))
