"""
3-10 ) 동전
 https://www.acmicpc.net/problem/11047

"""
# 값 입력 받음
n, k = map(int, input().split())
data = []

for i in range(n) :
    data.append(int(input())) 

data.sort(reverse=True)    

cnt = 0
for i in data :
    if i <= k :
        cnt += (k//i)
        k = k%i

print(cnt)