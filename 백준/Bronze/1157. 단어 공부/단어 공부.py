# 대문자로 전부 형변환 완료
test=input().upper()
test_list = list(set(test))

cnt=[]
for i in test_list:
    count = test.count
    cnt.append(count(i))

if cnt.count(max(cnt)) > 1:
    print("?")

else:
    print(test_list[(cnt.index(max(cnt)))])