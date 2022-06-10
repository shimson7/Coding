from collections import Counter

import sys

N=int(sys.stdin.readline())
num_list=[]

for i in range(N):
    num=int(sys.stdin.readline())
    num_list.append(num)
num_list.sort()


#첫째 줄 산술평균 출력 소수점 이하 첫째 자리 반올림 값
print(round(sum(num_list) / N))
#둘째 줄 중앙값
mid=N // 2
print(num_list[mid])
#셋째 줄 최빈값. 여러개 있을 시 두번째로 작은 값
cnt = Counter(num_list).most_common(2)

if len(num_list) > 1:
    if cnt[0][1] == cnt[1][1]:
        print(cnt[1][0])
    else:
        print(cnt[0][0])
else:
    print(cnt[0][0])
#넷째 줄 범위
if len(num_list)==1:
    print(0)
else:
    print(max(num_list)-min(num_list))
