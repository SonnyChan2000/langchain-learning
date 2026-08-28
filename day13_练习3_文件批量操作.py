import os

os.makedirs("test_files", exist_ok = True)

for i in range(1, 11):
    filepath = f"test_files/file_{i}.txt"
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(f"这是第{i}个文件")

print("10个文件创建完成")

files = os.listdir("test_files")
print("文件列表：", files)

if os.path.exists(os.path.join("test_files", input("请输入需要查找的文件名: "))):
    print("存在")
else:
    print("不存在")