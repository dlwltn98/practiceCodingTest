"""
4-2 ) 시각
 
"""
# 값 입력 받음
h = int(input())

cnt = 0
# 3이 포함되어 있는지 확인
for i in range(h+1) :
    for j in range(60) :
        for z in range(60) :
            if '3' in str(i) + str(j) + str(z) :
                cnt += 1

print(cnt)