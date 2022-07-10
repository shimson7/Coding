def solution(arr1, arr2):
    answer = []

    #arr1 전체 길이만큼 돌아야함
    for i in range(len(arr1)):
        #0, 1
        add_answer=[]
        #arr1 첫번째 리스트 길이만큼 돌아야함
        for j in range(len(arr1[0])):
            #0, 1
            add_answer.append(arr1[i][j]+arr2[i][j])
        answer.append(add_answer)
    # print(answer)
    return answer