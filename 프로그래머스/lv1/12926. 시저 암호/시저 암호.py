def solution(s, n):
    answer = []
    # A 65 Z 90 a 97 z 122
    for i in range(len(s)):
        alpha=ord(s[i])
        letter = alpha + n
        if 65<=alpha and alpha<=90: #대문자일때
            if letter>90:
                letter=64+(letter-90)
            answer.append(chr(letter))
        elif 97<=alpha and alpha<=122: # 소문자일때
            if letter>122:
                letter=96+(letter-122)
            answer.append(chr(letter))
        elif alpha==32: #스페이스가 들어왔을때 스페이스값 추가
            answer.append(chr(32))
    dap=''
    for j in range(len(answer)):
        dap+=answer[j]

    return dap