import sys

if __name__ == '__main__':
    sentence = sys.stdin.read()
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    result = []

    for i in alphabet:
        result.append(sentence.count(i))

    m = max(result)
    for i in range(len(result)):
        if m == result[i]:
            print(chr(i+97), end='')