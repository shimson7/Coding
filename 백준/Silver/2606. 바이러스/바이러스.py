from collections import deque

def BFS(graph, root):
    visited = []
    queue = deque([root])

    while queue:
        n = queue.popleft()
        if n not in visited:
            visited.append(n)
            if n in graph:
                temp = list(set(graph[n]) - set(visited))
                temp.sort()
                queue += temp
    # return " ".join(str(i) for i in visited)
    return len(visited)-1

graph={}

n=int(input())
edge=int(input())

for i in range(edge):
    edge_info=input().split()
    n1, n2 = [int(j) for j in edge_info]
    if n1 not in graph:
        graph[n1]=[n2]
    elif n2 not in graph[n1]:
        graph[n1].append(n2)

    if n2 not in graph:
        graph[n2]=[n1]
    elif n1 not in graph[n2]:
        graph[n2].append(n1)



print(BFS(graph, 1))