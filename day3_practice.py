# ==== 用三元表达式判断奇偶 ====
num = 12 
result = "偶数" if num % 2 == 0 else "奇数"
print(f"{num}是{result}")


# ==== 取两个数中较大的 ====
a = 17
b = 8
max_val = a if a > b else b
print(f"a和b中较大的是{max_val}")


# ==== 成绩是否及格 ====
score = 95
status = "及格" if score >= 60 else "不及格"
print(f"{score}分,{status}")


# ==== 嵌套if ====
age = 25
has_ticket = True
is_vip = False

if age >= 18:
    if has_ticket:
        if is_vip:
            print("vip通道入场")
        else:
            print("普通通道入场")
    else:
        print("请先买票")
else:
    print("未成年人不能入场")


# ==== 复合条件(在if里用and和or) ====
score = 59
attendance = 0.8

if score >= 80 and attendance >= 0.8:
    print("成绩优秀且出勤良好")
elif score >= 60 or attendance >= 0.9:
    print("成绩或出勤至少一项达标") 
else:
    print("需要加油")
