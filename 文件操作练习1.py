article = ["第一行\n", "第二行\n", "第三行\n", "第四行\n", "第五行\n"]
with open("article.txt", "w", encoding="utf-8") as f:
    f.writelines(article)

count = 0
line_count = 0
with open("article.txt", "r", encoding="utf-8") as f:
    for line in f:
        count += len(line.strip())
        line_count += 1

print(f"共{len(article)}行, 共{count}字")
