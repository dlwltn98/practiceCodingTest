"""
3-7 ) 문자열 뒤집기

"""
# 값 입력 받기
s = input()

# 값이 바뀐것 체크
cnt0 = 0
cnt1 = 0

if s[0] == '0' :
    cnt0 += 1
else :
    cnt1 += 1

for i in range(len(s)-1) :
    if s[i] != s[i+1] :
        if s[i+1] == '0' :
            cnt0 += 1
        else :
            cnt1 += 1
    
print(min(cnt0, cnt1))



