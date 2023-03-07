"""
4-5 ) 문자열 재정렬
 
"""
import re

# 값 입력 
str = input()

# 숫자만 추출
strNum = re.findall('\d', str)
strNum.sort()

# 문자만 추출 
strStr = re.findall('[a-zA-Z]', str)
strStr.sort()

str = strStr + strNum
print ("".join(str))