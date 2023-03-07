"""
3-8 ) 만들 수 없는 금액

"""
# 값 입력 받기
n = int(input())
data = list(map(int, input().split()))

# 데이터 정렬
data.sort()

t = 1
for i in data : 
    if t < i :
        break
    t += i

print(t)
