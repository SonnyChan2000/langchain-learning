while True:
    print("="*30 + "日记本程序" + "="*30)
    print("1. 写日记")
    print("2. 查看所有日记")
    print("3. 退出")

    choice = int(input("请输入你的选择："))

    if choice == 1:
        with open("diary.txt", "a", encoding="utf-8") as f:
            f.write(input("请输入日期：\n") + "\n")
            f.write(input("请输入日记内容:") + "\n")

    elif choice == 2:
        with open("diary.txt", "r", encoding="utf-8") as f:
            for line in f:
                print(line.strip())

    elif choice == 3:
        break
    else:
        print("输入错误")
                    


