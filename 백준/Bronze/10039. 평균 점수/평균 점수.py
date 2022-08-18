score_list=[]

for _ in range(5):
    score=int(input())

    if score<40:
        score=40
    score_list.append(score)

print(sum(score_list)//5)