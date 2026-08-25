students = [
    {"姓名": "张三", "语文": 85, "数学": 92, "英语": 78},
    {"姓名": "李四", "语文": 90, "数学": 88, "英语": 95},
    {"姓名": "王五", "语文": 72, "数学": 65, "英语": 80}
]

for student in students:
    student["平均分"] = (student["语文"] + student["数学"] + student["英语"]) / 3

mathmax_student = students[0]
for student in students:
    if student["数学"] > mathmax_student["数学"]:
        mathmax_student = student
print(f"数学成绩最高的是{mathmax_student['姓名']}, 分数是{mathmax_student['数学']}")

sorted_students = sorted(students, key = lambda s:s["平均分"], reverse = True)
for s in sorted_students:
    print(f"{s['姓名']}: {s["平均分"]:.1f}")

English_total = 0
for student in students:
    English_total += student["英语"]
English_average = English_total / len(students)
print(f"英语成绩平均分为：{English_average:.1f}")
