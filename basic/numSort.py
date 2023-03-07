"""
001 ) 수 정렬하기
 https://www.acmicpc.net/problem/2750

"""
# 값 입력 받기
n = int(input())

data =[]
for i in range(n) :
    data.append(int(input()))

data.sort()

for i in data :
    print(i)