from collections import deque
import sys

input=sys.stdin.readline

def DFS(graph,root):
    visited=[]
    stack = [root]

    while stack:
        n=stack.pop()
        if n not in visited:
            visited.append(n)
            if n in graph:
                temp = list(set(graph[n])-set(visited))
                temp.sort(reverse=True)
                stack += temp
    return " ".join(str(i) for i in visited)

def BFS(graph,root):
    visited=[]
    queue = deque([root])

    while queue:
        n=queue.popleft()
        if n not in visited:
            visited.append(n)
            if n in graph:
                temp = list(set(graph[n])-set(visited))
                temp.sort()
                queue += temp
    return " ".join(str(i) for i in visited)

graph = {}
N,M,V=map(int, input().split())
for i in range(M):
    M_info = input().split()
    n1, n2 = [int(j) for j in M_info]
    if n1 not in graph:
        graph[n1] = [n2]
    elif n2 not in graph[n1]:
        graph[n1].append(n2)

    if n2 not in graph:
        graph[n2] = [n1]
    elif n1 not in graph[n2]:
        graph[n2].append(n1)

print(DFS(graph,V))
print(BFS(graph,V))