for i in range(1 , 6):
    print(f"第{i}次循环")


# ==== 1到100求和 ====
total = 0

for i in range(1 , 101):
    total = total + i
print(f"1到100的总和是{total}")


# ==== while循环 ====
i = 1
while i <= 5:
    print(i)
    i += 1


# ==== break和continue ====
print("="*30 + "break和continue" + "=" * 30)
i = 0
while i < 10:
    i += 1
    if i == 5:
        continue
    if i == 8:
        break
    print(i)


# ==== 嵌套循环 ====
print("="*30 + "嵌套循环" + "=" * 30)
for i in range(1 , 4):
    for j in range(1 , 4):
        print(f"i={i}, j={j}")


# ==== 九九乘法表 ====
print("="*30 + "九九乘法表" + "=" * 30)
for i in range(1 , 10):
    for j in range(1,i+1):
        result = i * j
        print(f"{j}x{i}={result}", end="\t")
    print()


# ==== 1到100累加 while循环 ====
print("="*30 + "1到100累加 while循环" + "=" * 30)
total = 0
i = 1
while i <= 100:
    total += i
    i += 1
print(f"1到100的总和是{total}")


# ==== 打印金字塔图案 ====
print("="*30 + "打印金字塔图案" + "=" * 30)
for i in range(1 , 6):
    num1 = 5 - i
    num2 = i * 2 - 1
    print(" "*num1 + "*"*num2 + " "*num1)


# ==== 找出100以内所有素数 ====
print("="*30 + "找出100以内所有素数" + "=" * 30)

for i in range(2 , 101):
    is_prime = True
    for j in range(2 , i):
        if i % j == 0:
            is_prime = False
            break
    if is_prime == True:
        print(f"{i}" , end=" ")

