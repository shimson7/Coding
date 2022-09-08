import time

year=time.strftime('%Y', time.localtime(time.time()))
month=time.strftime('%m', time.localtime(time.time()))
day=time.strftime('%d', time.localtime(time.time()))
print(year)
print(month)
print(day)