for _ in range(int(input())):
    s = input()

    stack = []
    for c in s:
        if c == "(":
            stack.append(c)
        elif c == ")":
            if not stack or stack[-1] != "(":
                stack.append(")")
                break

            stack.pop()

    print("YES" if not stack else "NO")