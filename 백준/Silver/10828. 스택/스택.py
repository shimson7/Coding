import sys

N=int(sys.stdin.readline())
stack=[]

for i in range(N):
    cmd=sys.stdin.readline().split()
    cmd_list=list(cmd)
    #cmd가 push
    if cmd_list[0]=='push':
        stack.append(cmd_list[1])
    # cmd가 top일때
    elif cmd_list[0]=='top':
        if len(stack)==0:
            print(-1)
        else:
            print(stack[-1])
    # cmd가 size일때
    elif cmd_list[0]=='size':
        print(len(stack))
    # cmd가 pop일때
    elif cmd_list[0]=='pop':
        if len(stack)==0:
            print(-1)
        else:
            stack_pop=stack.pop()
            print(stack_pop)
    # cmd가 empty일때
    elif cmd_list[0]=='empty':
        if len(stack)==0:
            print(1)
        else:
            print(0)