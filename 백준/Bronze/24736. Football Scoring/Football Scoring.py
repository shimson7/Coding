A=list(map(int, input().split()))
B=list(map(int, input().split()))

A_score=(A[0]*6+A[1]*3+A[2]*2+A[3]*1+A[4]*2)
B_score=(B[0]*6+B[1]*3+B[2]*2+B[3]*1+B[4]*2)
print(A_score,B_score)