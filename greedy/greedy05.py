"""
3-5 ) 모험가 길드

"""
# 값 입력 받음
n = int(input())
data = list(map(int, input().split()))

# data의 값 들이 n 보다 작으면 가장 큰수-1
# data의 값 들이 n 보다 크면 n-1
result = 0
for i in data :
    if(i > n) :
        result = n-1
    else :
        result = max(data)-1

print(result)
