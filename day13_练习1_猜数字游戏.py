import random
num = random.randint(1, 100)
count = 0

while True:
    try:
        guess = int(input("请猜数: "))
        if guess == num:
            print(f"猜对了! 共猜了{count}次")
            break
        elif guess > num:
            print("大了")
            count += 1
        elif guess < num:
            print("小了")
            count += 1
    except ValueError:
        print("请输入有效数字")
