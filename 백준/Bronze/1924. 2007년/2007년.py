from datetime import date
M, D= map(int, input().split())
days=date(2007, M, D)
print(days.strftime('%a').upper())
