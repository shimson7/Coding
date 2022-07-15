from sys import stdin
n, m, b = map(int, stdin.readline().split())

map = [list(map(int, stdin.readline().split())) for _ in range(n)]

avg = 0
for i in range(n):
    avg += sum(map[i])

avg += b
avg //= (n*m)
result = []

height = 0
while height <= avg:
    time = 0
    for j in range(n):
        for i in range(m):
            gap = 0
            # 제거 후 저장
            if height < map[j][i]:
                gap = map[j][i] - height
                time += gap*2
            # 블록 추가
            elif height > map[j][i]:
                gap = height - map[j][i]
                time += gap
    result.append(time*1000000 + height)
    height += 1

max = min(result)
for i in range(len(result)):
    if result[i] // 1000000 == min(result) // 1000000 and max < result[i]:
        max = result[i]

print(max // 1000000, max % 1000000)