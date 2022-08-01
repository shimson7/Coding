'''
1번 12345 반복
2번 21 23 24 25 반복
3번 33 11 22 44 55 반복

for문 최대(10000):
    1번 i % 5
        answers와 같다면 +1
    2번 i % 8
        answers와 같다면 +1
    3번 i % 10
        answers와 같다면 +1
각각 맞은 개수 따로 리스트에 넣어서 확인하고 제일 높은 사람 return하게
'''

def solution(answers):
    answer = []
    one=[1,2,3,4,5]
    two=[2,1,2,3,2,4,2,5]
    three=[3,3,1,1,2,2,4,4,5,5]
    one_c=0
    two_c=0
    three_c=0
    for i in range(len(answers)):
        if answers[i%len(answers)]==one[i%5]:
            one_c+=1
        if answers[i%len(answers)]==two[i%8]:
            two_c+=1
        if answers[i%len(answers)]==three[i%10]:
            three_c+=1
    big=max(one_c,two_c,three_c)
    if one_c==big:
        answer.append(1)
    if two_c==big:
        answer.append(2)
    if three_c==big:
        answer.append(3)
    print(answer)
    return answer

answers=[1,2,3,4,5]
# answers=[1,3,2,4,2]
solution(answers)

