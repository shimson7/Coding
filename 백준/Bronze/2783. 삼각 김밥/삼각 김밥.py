x, y = map(int, input().split())
gs_min = x * 1000 / y
n = int(input())
for i in range(n):
    a, b = map(int, input().split())
    gs_min = min(gs_min, a * 1000 / b)
print(round(gs_min, 2))