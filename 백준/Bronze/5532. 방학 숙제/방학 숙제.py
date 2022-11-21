L = int(input())
A = int(input())
B = int(input())
C = int(input())
D = int(input())

lan=int(A/C)
lan1=A%C
math=int(B/D)
math1=B%D

if lan1>=1:
    lan=lan+1
if math1>=1:
    math=math+1

print(L-max(lan,math))