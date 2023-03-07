"""
3-6 ) 곱하기 혹은 더하기

"""

# 입력값 받기
s = input()

# 문자열을 배열로 변환
sList = list(map(int, s))

# 계산
result = 0
for i in sList :
    
    if(i == 0 or result == 0) :
        result += i
    else :
        result *= i

print(result)


