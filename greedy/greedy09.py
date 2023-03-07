"""
3-9 ) 볼링공 고르기

"""
# 값 입력 받기
n, m = map(int, input().split())
data = list(map(int, input().split()))


cnt = 0
for i in range(len(data)-1) :
    for j in range(i+1, len(data)) : 
        if data[i] != data[j] : 
            cnt += 1

print(cnt)

