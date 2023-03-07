"""
4-3 ) 왕실의 나이트
 
"""
# 값 입력 받기
inputData = input()

x = int(ord(inputData[0]) - ord('a')) + 1  # col
y = int(inputData[1])   # row

result = 0
# 이동할 수 있는 방향 정의
steps = [ (-1, 2), (1, 2) 
        , (2, -1), (2, 1)
        , (1, -2), (-1, -2)
        , (-2, -1), (-2, 1) 
        ]

for i in steps :
    nextX = x + i[0]
    nextY = y + i[1]

    if nextX >= 1 and nextX <= 8 and nextY >= 1 and nextY <= 8 :
        result += 1

print(result)