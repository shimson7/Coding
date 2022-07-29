def solution(sizes):
    L= len(sizes)
    sizes_w = 0
    sizes_h = 0

    for i in range(L):
        sizes[i].sort()
        sizes_w = max(sizes_w, sizes[i][0])
        sizes_h = max(sizes_h, sizes[i][1])
        
    return sizes_w*sizes_h