from collections import deque
import sys

d=deque()
N = int(sys.stdin.readline())

Deque = []

for i in range(N):
    cmd = sys.stdin.readline().split()

    if cmd[0] == "push_front":
        d.insert(0, int(cmd[1]))
        ##print(Deque)
    elif cmd[0] == "push_back":
        d.append(int(cmd[1]))

    elif cmd[0] == "pop_front":
        if len(d) != 0: print(d.popleft())
        else: print(-1)
    elif cmd[0] == "pop_back":
        if len(d) != 0: print(d.pop())
        else: print(-1)

    elif cmd[0] == "size":
        print(len(d))

    elif cmd[0] == "empty":
        if len(d) == 0: print(1)
        else : print(0)

    elif cmd[0] == "front":
        if len(d) == 0: print(-1)
        else: print(d[0])

    elif cmd[0] == "back":
        if len(d) == 0: print(-1)
        else: print(d[-1])