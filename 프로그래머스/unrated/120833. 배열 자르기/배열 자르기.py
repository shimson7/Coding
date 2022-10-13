def solution(numbers, num1, num2):
    answer = []
    for i in range(len(numbers)):
        if num1<=i and i<=num2:
            answer.append(numbers[i])
    
    return answer