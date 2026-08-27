score = [
    {"姓名": "张三", "语文": "64", "数学": "78", "英语": "90"},
    {"姓名": "李四", "语文": "70", "数学": "79", "英语": "70"},
    {"姓名": "王五", "语文": "80", "数学": "90", "英语": "85"}
]
import csv

with open("score.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["姓名", "语文", "数学", "英语"])
    for s in score:
        writer.writerow(
            [s["姓名"], s["语文"], s["数学"], s["英语"]]
        )

with open("score.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        name = row[0]
        average_score = (int(row[1]) + int(row[2]) + int(row[3])) / 3
        print(f"{name} 平均分:{average_score:.1f}")
