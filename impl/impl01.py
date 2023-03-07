"""
4-1 ) 상하좌우
 
"""
# 값 입력
n = int(input())  # 공간의 크기 (n, n)
data = list(map(str, input().split()))  # 이동 계획

result = [1, 1]  # 위치
for i in data : 
    # 위 
    if i == "U" and result[0] > 1 :
        result[0] -= 1

    # 아래
    if i == "D" and result[0] < n : 
        result[0] += 1

    # 완쪽
    if i == "L" and result[1] > 1 : 
        result[1] -= 1

    # 오른쪽 
    if i == "R" and result[1] < n : 
        result[1] += 1

print(result)