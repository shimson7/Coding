from collections import deque

def solution(s):
    answer=''
    queue=deque(s)
    while True:
        # print(queue[0])
        if queue[0]==max(queue):
            answer+=queue[0]
            queue.popleft()
        elif queue[0]!=max(queue):
            queue.append(queue.popleft())
        if len(answer)==len(s):
            break
    return answer