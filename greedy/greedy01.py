"""
3-1 ) 거스름돈
 카운터에는 거스름돈으로 사용할 500원, 100원, 50원, 10원짜리 동전이 무한히 존재.
 손님에게 거슬러 줘야 할 돈이 N원일 때 거슬러줘야 할 동전의 최소 개수 구하기
 단, 거슬러줘야 할 돈 N은 항상 10의 배수임 
"""

# 거슬러줘야 할 돈 입력
n = int(input())

# 단위가 큰 돈부터 나눔
list = [500, 100, 50]
cnt = 0

for coin in list:
    cnt += (n//coin)
    n %= coin

print(cnt)
