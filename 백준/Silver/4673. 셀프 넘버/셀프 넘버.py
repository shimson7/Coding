def self_number(num):
    self_num = num # 내가 넣은 인자
    while num != 0: # 몫이 0이 아니라면 계속 진행
        self_num += num % 10 # self_num = self_num + num % 10
        num //= 10 # num=num//10 몫이 담길것
    return self_num


result = []

for i in list(range(1, 10001)):
    result.append(self_number(i))
    if i not in result:
        print(i)