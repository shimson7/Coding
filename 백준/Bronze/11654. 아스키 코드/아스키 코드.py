ans=input() #문자열로 입력받음
tmp=ord(ans)

#알파벳 대문자 65~90
if 65<=tmp & tmp<=90:
    print(tmp)
#알파벳 소문자 97~122
elif 97<=tmp & tmp<=122:
    print(tmp)
#숫자 0~9 48~57
elif 48<=tmp & tmp<=57:
    print(tmp)
