'''
1. 구하고자 하는 수 N을 입력받는다.

2. N으로 나누었을 때 나머지와 몫이 같은 모든 자연수의 합 ans을 정의한다.

ex) N=5, 나머지와 몫이 같은 수는 5*1+1, 5*2+2, 5*3+3, 5*4+4. 즉 for문을 돌면서 N*i+i를 해주면 된다.

3. 1~N-1까지 for문을 돌면서 ans에 N*i+i을 더해준다.

4. ans을 출력한다.

'''

N=int(input())
ans=0
for i in range(1,N):
    ans+=(N*i+i)
print(ans)