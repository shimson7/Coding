T=int(input())
for i in range(T):
    answer_list=list(input())
    sum=0
    
    for j in answer_list:
        if j == '(':
            sum += 1
        elif j == ')':
            sum -= 1
        if sum < 0:
            print("NO")
            break
    if sum > 0:
        print("NO")
    elif sum == 0:
        print("YES")