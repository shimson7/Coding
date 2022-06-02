test=int(input()) # 테스트하는 횟수
cnt=test

for i in range(test):
    word=input() # 입력받는 곳
    for j in range(0, len(word)-1): # 길이가 4인 문자열이면 2번인덱스(세번째 글짜)까지 확인
        if word[j] == word[j + 1]:
            pass
        elif word[j] in word[j + 1:]: 
            cnt -= 1
            break

print(cnt)