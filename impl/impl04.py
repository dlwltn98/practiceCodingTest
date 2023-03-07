"""
4-4 ) 럭키 스트레이트
 
"""
# 값 입력 
n = input()
nList = [int(i) for i in n]

leftSum = 0
for i in range(len(nList)//2) :
    leftSum += nList[i]

rightSum = 0
nList.reverse()
for i in range(len(nList)//2) :
    rightSum += nList[i]

if leftSum == rightSum :
    print("Lucky")
else :
    print("READY")