import datetime

today = datetime.datetime.now()
target = datetime.datetime(2027, 1, 1)
diff = target - today
day = today + datetime.timedelta(days = 100)

print(f"今天是{today.strftime('%Y年%m月%d日')}")
print(f"距离2027年元旦还有: {diff.days}天")
print(f"100天后是: {day.strftime("%Y年%m月%d日")}")