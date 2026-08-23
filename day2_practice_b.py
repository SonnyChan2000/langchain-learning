# ==== 判断闰年小程序 ====
year = int(input("请输入需要判断的年份："))

if year % 4 == 0 and year % 100 != 0 :
    print("该年份是闰年")
elif year % 400 == 0:
    print("该年份是闰年")
else:
    print("该年份不是闰年")
    