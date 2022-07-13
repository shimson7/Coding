import datetime

now = datetime.datetime.now()
year=now.strftime("%Y")
month=now.strftime("%m")
day=now.strftime("%d")
print(year,end='-')
print(month,end='-')
print(day)