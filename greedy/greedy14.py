"""
3-14 ) 30
 https://www.acmicpc.net/problem/10610
 ++ 수정 필요
 
"""
# 값 입력
num = input()
num = [int(i) for i in num]

result = 0

# 30의 배수가 되기 위해선 0을 포함하고 합친 수가 3의 배수여야 함
if sum(num)%3 == 0 and 0 in num : 
    print("".join(map(str,sorted(num,reverse=True))))
else : 
    result = -1

print(result)
