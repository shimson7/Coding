def mathematics():
    answer = 0
    time=int(input())
    for _ in range(time):
        try:
            num = int(input())
            answer += num
        except EOFError:
            break

    return answer


if __name__ == "__main__":
    print(mathematics())