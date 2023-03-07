"""
3-12 ) 잃어버린 괄호
 https://www.acmicpc.net/problem/1541
 
 '-'를 기준으로 끊어서 계산
"""
# 값 입력 받음
num = input().split("-")

result = sum(map(int, num[0].split("+")))

for i in num[1:] : 
    result -= sum(map(int, i.split("+")))

print(result)
