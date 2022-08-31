bet_list=[]

while True:
    bet=int(input())
    if bet==-1:
        break
    bet_list.append(bet)

print(sum(bet_list))