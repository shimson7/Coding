def solution(arr):
    answer = []
    answer.append(arr[0])
    for i in range(1,len(arr)): #0
        if arr[i] != answer[-1]: #1
            answer.append(arr[i])  # 1
    # print(answer)
    return answer