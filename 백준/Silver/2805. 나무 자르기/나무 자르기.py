N, M = map(int, input().split()) # 나무의 수, 집으로 가져가려고 하는 나무 길이

tree_list=list(map(int, input().split()))
min_height=0
max_height=max(tree_list)
answer=0
while min_height <= max_height :
    mid = (min_height+max_height)//2
    num = 0
    for tree in tree_list :
        if tree > mid :
            num += tree - mid
        if num >= M :
            break
    if num >= M :
        answer = max(answer, mid)
        min_height = mid + 1
    else :
        max_height = mid - 1
print(answer)