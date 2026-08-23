# ==== 猜数字游戏 ====
import random
answer = random.randint(1 , 100)

count = 0 
while True:
    count += 1
    guess = int(input("请输入你猜的数字："))
    if guess == answer:
        print(f"猜对了！一共猜了{count}次")
        break
    elif guess < answer:
        print("小了")
    else:
        print("大了")
    


