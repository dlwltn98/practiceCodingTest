"""
3-13 ) 대회 or 인턴
 https://www.acmicpc.net/problem/2875
 
"""
# 값 입력
# 여학생, 남학생, 인턴쉽
n, m, k = map(int, input().split())

for i in range(k) :
    if n//2 >= m : 
        n -= 1
    else :
        m -= 1

print(min(m, n//2))