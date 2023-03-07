"""
3-2 ) 큰 수 
 다양한 수로 이루어진 배열이 있을때 주어진 수들을 M번 더하여 가장 큰 수를 만드는 법칙
 단, 배열의 특정한 인엑스에 해당하는 수가 연속해서 K번을 초과하여 더해질 수 없다
"""
"""

# 값 입력 받음
# n = 입력 받을 수의 갯수, m = 더함, k = 연속 
n, m, k = map(int, input().split())

# n개의 수 공백으로 구분하여 입력 받음
data = list(map(int, input().split()))

# data 정렬
data.sort()

# 가장 큰 수 2개 찾기
firstData = data[n-1]
secondData = data[n-2]

# 계산
result = 0

while True:
    if m == 0 :
        break
    
    for i in range(0,k) :
        result += firstData
        m -= 1
        if(m==0):
            break

    result += secondData
    m -= 1

print(result)

"""
"""
3-2-1 ) 큰 수 (다른 풀이) 
 반복되는 수열의 길이 : K + 1
 반복 횟수 : N / (K + 1)
 큰 수가 등장하는 횟수 : N / (K + 1) * k
 나누어 떨어지지 않을 경우 나머지 값 만큼 큰 수 더함 : N % (K + 1)
 큰 수가 더해지는 수 : N / (K + 1) * k + N % (K + 1)
"""

# 값 입력 받음
# n = 입력 받을 수의 갯수, m = 더함, k = 연속 
n, m, k = map(int, input().split())
data = list(map(int, input().split()))

# 입력 받은 데이터 리스트 정렬
data.sort()

# 가장 큰 수 2개 찾기
firstData = data[n-1]
secondData = data[n-2]

# 큰 수가 더해지는 수
# N / (K + 1) * k + N % (K + 1)
cnt = m//(k+1) * k + m%(k+1) 

#결과
result =0
result += firstData * cnt
result += secondData * (m-cnt)

print(result)