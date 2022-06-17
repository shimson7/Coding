def get_hansu_num(N):
    if N<100:
        hansu = N
    else:
        hansu = 99
        for i in range(100, N+1):
            num_list = list(map(int, str(i)))
            
            if num_list[0] - num_list[1] == num_list[1] - num_list[2]:
                hansu += 1
    return hansu

print(get_hansu_num(int(input())))