import sys

n, m = map(int, sys.stdin.readline().split())
site = dict() # 딕셔너리형

# 반복문을 통해 사이트의 주소와 비밀번호를 입력받아 딕셔너리에 담는다.
for _ in range(n):
    id, pw = map(str, sys.stdin.readline().split())
    site[id] = pw

# 반복문을 통해 찾고자 하는 주소의 비밀번호를 출력한다.
for _ in range(m):
    address = str(sys.stdin.readline().rstrip())
    print(site[address])