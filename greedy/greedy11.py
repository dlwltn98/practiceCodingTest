"""
3-11 ) ATM
 https://www.acmicpc.net/problem/11399

"""
# 값 입력 받음
n = int(input())
data= list(map(int, input().split()))

#for i in range(n) :
#    data.append(int(input()))


data.sort()

# 계산
result = 0
for i in range(len(data)) : 
    if i != 0 :
        for j in range(0, i+1):
            result += data[j]
    else : 
        result += data[i]

print(result)