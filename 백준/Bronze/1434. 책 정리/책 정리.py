import sys
input = sys.stdin.readline

# 입력
N, M = map(int, input().split())
box = list(map(int, input().split()))
book = list(map(int, input().split()))

# 책 정리
idx = 0  # 박스 넘버
for b in book:
    # 책이 박스에 들어갈 때까지 박스 교체
    while True:
        # 책이 박스에 들어감
        if b <= box[idx]:
            box[idx] -= b
            break

        # 책이 박스에 안 들어가면, 박스 교체
        idx += 1
print(sum(box))