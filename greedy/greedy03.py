"""
3-3 ) 숫자 카드 게임

"""

# 값 입력 받음
# N : 행의 개수, M : 열의 개수
n, m = map(int, input().split())

result = 0

# 행의 수 만큼 반복
for i in range(n) :
    
    # 행별로 데이터 받음
    data = list(map(int, input().split()))

    minVal = min(data)
    result = max(result, minVal)

print(result)

