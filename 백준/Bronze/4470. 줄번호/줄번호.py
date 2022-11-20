N = int(input())
sentences=list()
for i in range(N):
    sentences.append(input())

for j in range(len(sentences)):
    print(str(j+1)+". "+sentences[j])
