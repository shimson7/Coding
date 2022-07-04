import sys
input = sys.stdin.readline

while True:
    words = input().rstrip()
    if words == '.':
        break

    stack = []
    flag = False
    for word in words:
        if word == '(':
            stack.append(word)
        elif word == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                flag = True
                break

        elif word == '[':
            stack.append(word)
        elif word == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                flag = True
                break

    if flag or stack:
        print('no')

    elif not stack:
        print('yes')