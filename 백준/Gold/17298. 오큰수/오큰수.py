N = int(input())
A = list(map(int, input().split()))

NGE = [-1] * N
stack = []
for i in range(N) :
    while(len(stack) != 0 and A[stack[-1]] < A[i]) :
        NGE[stack[-1]] = A[i]
        stack.pop()
    stack.append(i)
print(*NGE)