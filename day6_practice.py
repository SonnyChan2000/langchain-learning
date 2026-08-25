# ==== 字典dic ====
student = {"姓名": "张三", "年龄": 25, "专业": "机械", "是否毕业": True}
print(student["姓名"])
print(student["年龄"])

student["年龄"] = 28
print(student["年龄"])

student["城市"] = "杭州"

del student["是否毕业"]

print(student.get("电话"))
print(student.get("电话", "未填写"))

# ==== 遍历字典 ====
print("="*30 + "遍历字典" + "=" * 30)

for key in student.keys():
    print(key , end=" ")
print()

for value in student.values():
    print(value , end=" ")
print()

for key, value in student.items():
    print(f"{key}: {value}")

for key in student:
    print(key, end= " ")
print()


# ==== 字典嵌套 ====
print("="*30 + "字典嵌套" + "=" * 30)

student = {
    "张三": {"年龄": 25, "专业": "机械", "成绩": 85},
    "李四": {"年龄": 24, "专业": "计算机", "成绩": 92},
    "王五": {"年龄": 26, "专业": "电子", "成绩": 78}
}

print(student["张三"]["年龄"])
print(student["李四"]["成绩"])

for name,info in student.items():
    print(f"{name}: 年龄是{info['年龄']}, 专业是{info["专业"]}, 成绩是{info["成绩"]}")


# ==== 字典嵌套列表 ====
print("="*30 + "字典嵌套列表" + "=" * 30)

class_info = {
    "班级": "AI学习1班",
    "学生": ["张三", "李四", "王五"]
}

print(class_info["学生"][0])
print(class_info["班级"])

for student in class_info["学生"]:
    print(student)

print("班级" in class_info)
print("年龄" in class_info)

age = class_info.pop("学生")
print(age)
print(class_info)
print(len(class_info))

extra = {
    "城市": "杭州",
    "电话": "110"
}
class_info.update(extra)

print(class_info)