import sys

n, c, w = map(int, sys.stdin.readline().split())
trees = [int(sys.stdin.readline()) for _ in range(n)]
max_money = 0

# 반복문을 통해 나무를 1부터 제일 긴 나무의 길이만큼 잘라본다.
for i in range(1, max(trees) + 1):
    money = 0

    # 반복문을 통해 나무를 확인
    for j in trees:
        # cnt : 자른 나무 수
        # remain : 남은 나무의 길이
        cnt, remain = divmod(j, i)

        # 나무가 남았다면 자른 나무 수만큼 비용을 낸다.
        if remain:
            expense = cnt * c

        # 나무가 남지 않았다면 자른 나무 수 - 1만큼 비용을 낸다.
        else:
            expense = (cnt - 1) * c

        # 자른 나무를 판다.
        target = (cnt * w * i) - expense

        # 자른 나무를 팔 때 이익이 안난다면 continue
        if target < 0:
            continue

        # money에 이익을 더한다.
        money += target

    # 이익의 총합이 가장 큰 결과를 찾는다.
    if money >= max_money:
        max_money = money

print(max_money)