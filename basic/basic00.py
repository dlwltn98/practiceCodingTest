# 파이썬 문법 정리

"""
000-1 ) 몫 구하기
 https://school.programmers.co.kr/learn/courses/30/lessons/120805

"""
def solution(num1, num2):
    answer = num1 // num2
    return answer

"""
000-2 ) 나머지 구하기
 https://school.programmers.co.kr/learn/courses/30/lessons/120810

"""
def solution(num1, num2):
    answer = num1%num2
    return answer

"""
000-3 ) 자릿수 더하기
 https://school.programmers.co.kr/learn/courses/30/lessons/120906

"""
def solution(n):
    answer = 0
    n = list(str(n))
    
    for i in n :
        answer += int(i)
        
    return answer

"""
000-4 ) 문자열 안에 문자열 
 https://school.programmers.co.kr/learn/courses/30/lessons/120908

    * 문자열에서 특정 문자를 찾을 때 -> 문자열.find(찾으려는 문자), 존재O : 위치 반환, 존재X : -1 반환
 """
def solution(str1, str2):
    answer = 0
    
    if str1.find(str2) < 0 :
        return 2
    else :
        return 1

"""
000-5 ) 세균 증식
 https://school.programmers.co.kr/learn/courses/30/lessons/120910

"""    
def solution(n, t):
    for i in range(1, t+1) :
        n *= 2
    return n    

"""
000-6 ) 두 수의 차
 https://school.programmers.co.kr/learn/courses/30/lessons/120803

"""    
def solution(num1, num2):
    return num1 - num2

"""
000-7 ) 두 수의 곱
 https://school.programmers.co.kr/learn/courses/30/lessons/120804

"""   
def solution(num1, num2):
    return num1 * num2

"""
000-8 ) 나이 출력 
 https://school.programmers.co.kr/learn/courses/30/lessons/120820

"""   
def solution(age): 
    return 2023 - age

"""
000-9 ) 숫자 비교하기
 https://school.programmers.co.kr/learn/courses/30/lessons/120807

"""   
def solution(num1, num2):
    if num1 == num2 :
        return 1
    else :
        return -1
    
"""
000-10 ) 두 수의 합
 https://school.programmers.co.kr/learn/courses/30/lessons/120802

"""   
def solution(num1, num2):
    return num1 + num2

"""
000-11 ) 각도기
 https://school.programmers.co.kr/learn/courses/30/lessons/120829

    조건문 - if ~ elif ~ else
"""   
def solution(angle):
    if 0 < angle < 90 :
        return 1
    elif angle == 90 :
        return 2
    elif 90 < angle < 180 :
        return 3
    elif angle == 180 :
        return 4
    
"""
000-12 ) 두 수의 나눗셈
 https://school.programmers.co.kr/learn/courses/30/lessons/120806

      소수점 아래 버림 - math.trunc()

"""   
import math

def solution(num1, num2):
    answer = (num1/num2) * 1000
    return math.trunc(answer)

"""
000-13 ) 배열의 평균 값
 https://school.programmers.co.kr/learn/courses/30/lessons/120817

"""
def solution(numbers):
    answer = 0
    for i in numbers :
        answer += i
        
    return answer / len(numbers)   

"""
000-14 ) 짝수의 합
 https://school.programmers.co.kr/learn/courses/30/lessons/120831

"""   
def solution(n):
    answer = 0
    
    for i in range(1, n+1) :
        if i % 2 == 0 :
            answer += i
        
    return answer

"""
000-15 ) 양꼬치
 https://school.programmers.co.kr/learn/courses/30/lessons/120830

"""  
def solution(n, k):
    answer = n * 12000
    
    if n >= 10 :
        k -= n//10
        
    answer += k * 2000
    return answer 

"""
000-16 ) 피자 나눠 먹기(3)
 https://school.programmers.co.kr/learn/courses/30/lessons/120816

      소수점 올림 함수 - math.ceil()
"""   
import math

def solution(slice, n):
    return math.ceil(n/slice)

"""
000-17 ) 점의 위치 구하기
 https://school.programmers.co.kr/learn/courses/30/lessons/120841

"""
def solution(dot):
    if dot[0] > 0 and dot[1] > 0 :
        return 1
    elif dot[0] < 0 and dot[1] > 0 :
        return 2
    elif dot[0] < 0 and dot[1] < 0 :
        return 3
    elif dot[0] > 0 and dot[1] < 0 :
        return 4   

"""
000-18 ) 배열 뒤집기
 https://school.programmers.co.kr/learn/courses/30/lessons/120821

    배열 역순 출력 -> 리스트 슬라이싱 : 배열명[::-1]
"""   
def solution(num_list):
    return num_list[::-1]

"""
000-19 ) 배열 원소의 길이
 https://school.programmers.co.kr/learn/courses/30/lessons/120854

    배열에 요소 추가 - append()
"""   
def solution(strlist):
    answer = []
    
    for i in strlist :
        answer.append(len(i))
    return answer

"""
000-20 ) 짝수 홀수 개수
 https://school.programmers.co.kr/learn/courses/30/lessons/120824

"""
def solution(num_list):
    add = 0
    even = 0
    
    for i in num_list :
        if i % 2 == 0 :
            even += 1
        else :
            add += 1
    return [even, add]

"""
000-21 ) 삼각형의 완성조건 (1)
 https://school.programmers.co.kr/learn/courses/30/lessons/120889

    배열의 특정 요소 지우는 함수 : remove()
    배열의 최대 값을 찾는 함수 : max()
"""   
def solution(sides):
    
    long = max(sides)
    sides.remove(long)
    
    if long < sides[0] + sides[1] :
        return 1
    else :
        return 2

"""
000-22 ) 피자 나눠 먹기(1)
 https://school.programmers.co.kr/learn/courses/30/lessons/120814

"""   
import math

def solution(n):
    return math.ceil(n/7)

"""
000-23 ) 배열 자르기
 https://school.programmers.co.kr/learn/courses/30/lessons/120833

"""  
def solution(numbers, num1, num2):
    return numbers[num1:num2+1] 

"""
000-24 ) 중복된 숫자 개수 
 https://school.programmers.co.kr/learn/courses/30/lessons/120583

    개수 세는 함수 : count()
"""   
def solution(array, n):
    return array.count(n)

"""
000-25 ) 머쓱이보다 키 큰 사람 
 https://school.programmers.co.kr/learn/courses/30/lessons/120585

"""  
def solution(array, height):
    answer = 0
    for i in array :
        if height < i :
            answer += 1
    return answer

"""
000-26 ) 최댓값 만들기(1)
 https://school.programmers.co.kr/learn/courses/30/lessons/120847

    배열 역순 정렬 : sorted(정렬할 배열, reverse = True)
""" 
def solution(numbers):
    arr = sorted(numbers, reverse = True)
    return arr[0] * arr[1]

"""
000-27 ) 문자열 뒤집기
 https://school.programmers.co.kr/learn/courses/30/lessons/120822

""" 
def solution(my_string):
    return my_string[::-1]

"""
000-28 ) 특정 문자 제거하기
 https://school.programmers.co.kr/learn/courses/30/lessons/120826

""" 
def solution(my_string, letter):
    return my_string.replace(letter, "")

"""
000-29 ) 문자 반복하기
 https://school.programmers.co.kr/learn/courses/30/lessons/120825

"""
def solution(my_string, n):
    answer = ''
    for i in my_string :
        for j in range(0,n) :
            answer += i
    return answer 

"""
000-30 ) 배열 두 배 만들기
 https://school.programmers.co.kr/learn/courses/30/lessons/120809

""" 
def solution(numbers):
    answer = []
    for i in numbers :
        answer.append(i*2)
    return answer

"""
000-31 ) 옷 가게 할인 받기
 https://school.programmers.co.kr/learn/courses/30/lessons/120818

""" 
def solution(price):
    if price >= 500000:
        return int(price*0.8)
    elif price >= 300000 and price < 500000:
        return int(price * 0.9)
    elif price >= 100000 and price < 300000:
        return int(price * 0.95)
    else:
        return int(price)
    
"""
000-32 ) 배열의 유사도 
 https://school.programmers.co.kr/learn/courses/30/lessons/120903

"""     
def solution(s1, s2):
    answer = 0
    for i in s1 :
        for j in s2 :
            if i == j :
                answer += 1
    return answer

"""
000-33 ) 순서쌍의 개수 
 https://school.programmers.co.kr/learn/courses/30/lessons/120836

"""    
def solution(n):
    answer = 0
    for i in range(1, n+1) :
        if n%i == 0:
            answer +=1
    return answer 

"""
000-34 ) 아이스 아메리카노
 https://school.programmers.co.kr/learn/courses/30/lessons/120819

"""    
def solution(money):
    answer = []
    answer.append(money//5500)
    answer.append(money%5500)
    return answer 

"""
000-35 ) 짝수는 싫어요
 https://school.programmers.co.kr/learn/courses/30/lessons/120813

"""     
def solution(n):
    answer = []
    for i in range(1, n+1) :
        if i%2 != 0 :
            answer.append(i)
    return answer

"""
000-36 ) 편지
 https://school.programmers.co.kr/learn/courses/30/lessons/120898

"""
def solution(message):
    return len(message)*2 

"""
000-37 ) 중앙값 구하기
 https://school.programmers.co.kr/learn/courses/30/lessons/120811

""" 
import math

def solution(array):
    arr = sorted(array)
    return arr[math.trunc(len(array)/2)] 

"""
000-38 ) 숨어있는 숫자의 덧셈(1)
 https://school.programmers.co.kr/learn/courses/30/lessons/120851

    문자열에 숨어 있는 숫자 찾기 : re.sub(r'[^0-9]', '', 찾을 문자열)
"""  
import re

def solution(my_string):
    answer = 0
    numbers = re.sub(r'[^0-9]', '', my_string)
    for i in numbers :
        answer += int(i)
    return answer

"""
000-39 ) 모음제거
 https://school.programmers.co.kr/learn/courses/30/lessons/120849

"""  
def solution(my_string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    for i in vowels :
        my_string = my_string.replace(i, "")
    return my_string

"""
000-40 ) 개미군단
 https://school.programmers.co.kr/learn/courses/30/lessons/120837

"""  
def solution(hp):
    answer = 0
    ants = [5, 3, 1]
    
    for i in ants :
        answer += hp//i
        hp = hp%i
        if hp == 0 :
            break
    return answer

"""
000-41 ) 제곱수 판별하기
 https://school.programmers.co.kr/learn/courses/30/lessons/120909

"""  
def solution(n):
    sqrt = n ** (1/2)

    if sqrt % 1 == 0:
        return 1
    else :
        return 2

"""
000-42 ) 가위 바위 보
 https://school.programmers.co.kr/learn/courses/30/lessons/120839

"""  
def solution(rsp):
    answer = ''
    arr = list(rsp)
    
    for i in arr :
        if int(i) == 2 :
            answer += '0'
        if int(i) == 0 :
            answer += '5'
        if int(i) == 5 :
            answer += '2'
            
    return answer

"""
000-43 ) 암호 해독
 https://school.programmers.co.kr/learn/courses/30/lessons/120892

"""  
def solution(cipher, code):
    answer = ''
    arr = list(cipher)
    
    for i in range(1,len(arr)+1) :
        if i % code == 0 :
            answer += arr[i-1]
    
    return answer

"""
000-44 ) 대문자와 소문자
 https://school.programmers.co.kr/learn/courses/30/lessons/120893

    대문자가 있는지 확인 : isupper()
    소문자가 있는지 확인 : islower()
    소문자를 대문자로 변환 : upper()
    대문자를 소문자로 변환 : lower()
"""  
def solution(my_string):
    answer = ''
    arr = list(my_string)
    
    for i in arr :
        if i.isupper() :
            answer += i.lower()
        else :
            answer += i.upper()
            
    return answer

"""
000-45 ) 문자열 정렬하기
 https://school.programmers.co.kr/learn/courses/30/lessons/120850

"""  
import re

def solution(my_string):
    numbers = list(map(int, re.sub(r'[^0-9]', '', my_string)))
    return sorted(numbers)

"""
000-46 ) n의 배수 고르기
 https://school.programmers.co.kr/learn/courses/30/lessons/120905

"""  
def solution(n, numlist):
    answer = []
    for i in numlist :
        if i % n == 0 :
           answer.append(i)
    return answer

"""
000-47 ) 직각 삼각형 출력하기 
 https://school.programmers.co.kr/learn/courses/30/lessons/120823

    줄 바꿈 없이 출력 : print(출력할 내용, end='')
"""  
n = int(input())

for i in range(0, n) :
    for j in range(0, i+1) :
        print("*", end='')
    print("")

"""
000-48 ) 주사위의 개수 
 https://school.programmers.co.kr/learn/courses/30/lessons/120845

"""  
def solution(box, n):
    answer = []
    result = 1
    
    for i in box :
        answer.append(i//n)
        
    for i in answer :
        result *= i
    
    return result

"""
000-49 ) 최댓값 만들기 (2)
 https://school.programmers.co.kr/learn/courses/30/lessons/120862

"""
def solution(numbers):
    sortNum = sorted(numbers)
    
    maxNum = sortNum[len(sortNum)-1] * sortNum[len(sortNum)-2]
    if maxNum < sortNum[0] * sortNum[1] :
        maxNum = sortNum[0] * sortNum[1]
        
    return maxNum  

"""
000-50 ) 인덱스 바꾸기 
 https://school.programmers.co.kr/learn/courses/30/lessons/120895

    배열 문자열로 바꾸기 : "".join()
"""
def solution(my_string, num1, num2):
    arr = list(my_string)
    tmp = arr[num1]
    arr[num1] = arr[num2]
    arr[num2] = tmp
    
    return "".join(arr)

"""
000-51 ) 가장 큰 수 찾기
 https://school.programmers.co.kr/learn/courses/30/lessons/120899

    배열에서 특정 값의 위치값 찾기 : .index()
"""
def solution(array):
    answer = []
    
    answer.append(max(array))
    answer.append(array.index(answer[0]))    
    
    return answer

"""
000-52 ) 배열 회전 시키기
 https://school.programmers.co.kr/learn/courses/30/lessons/120844

    특정 위치의 배열 값 삭제 
        .pop() : 맨 마지막 값 삭제
        .pop(0) : 0번째 값 삭제
    특정 위치에 값 추가 : .insert(추가 할 위치, 추가할 값)
"""
def solution(numbers, direction):
    
    if direction == "left" :
        numbers.append(numbers[0])
        numbers.pop(0)
    else :
        numbers.insert(0, numbers[len(numbers)-1])
        numbers.pop()
        
    return numbers

"""
000-53 ) 외계행성의 나이
 https://school.programmers.co.kr/learn/courses/30/lessons/120834

"""
def solution(age):
    answer = ''
    arr = list(map(int, str(age)))
    age926 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    
    for i in arr :
        answer += age926[i]
    return answer

"""
000-54 ) 피자 나눠 먹기 (2)
 https://school.programmers.co.kr/learn/courses/30/lessons/120815

"""
def solution(n):
    i = 1
    result = 0
    while True :
        if n*i % 6 == 0 :
            result = n*i // 6
            break
        else :
            i += 1
    return result

"""
000-55 ) 약수 구하기 
 https://school.programmers.co.kr/learn/courses/30/lessons/120897

"""
def solution(n):
    result = []
    for i in range(1, n+1) :
        if n % i == 0 :
            result.append(i)
            
    return sorted(result)

"""
000-56 ) 숫자 찾기
 https://school.programmers.co.kr/learn/courses/30/lessons/120904

"""
def solution(num, k):
    if str(num).find(str(k)) >= 0 :
        return str(num).find(str(k))+1
    else :
        return -1

"""
000-57 ) 639 게임
 https://school.programmers.co.kr/learn/courses/30/lessons/120891

"""
def solution(order):
    answer = 0
    arr = list(map(int, str(order)))
    for i in arr :
        if i == 3 or i == 6 or i == 9 :
            answer += 1
    return answer

"""
000-58 ) 문자열 정렬하기(2)
 https://school.programmers.co.kr/learn/courses/30/lessons/120911

"""
def solution(my_string):
    return "".join(sorted(my_string.lower()))

"""
000-59 ) 합성수 찾기
 https://school.programmers.co.kr/learn/courses/30/lessons/120846

"""
def solution(n):
    answer = 0
    
    for i in range(1, n+1) :
        cnt = 0
        for j in range(1, i+1) :
            if i%j == 0 :
                cnt += 1
                
        if cnt >= 3 :
            answer += 1
    
    return answer

"""
000-60 ) 중복된 문자열 제거
 https://school.programmers.co.kr/learn/courses/30/lessons/120888

    dict.fromkeys(seq, value) : 딕셔너리를 생성할 때 편리하게 사용할 수 있는 메소드
    아래와 같이 쓰면 중복 제거 가능
"""
def solution(my_string):
    return "".join(dict.fromkeys(my_string))

"""
000-61 ) 모스부호 (1)
 https://school.programmers.co.kr/learn/courses/30/lessons/120838

"""
def solution(letter):
    answer = ''
    morse = { 
    '.-':'a','-...':'b','-.-.':'c','-..':'d','.':'e','..-.':'f',
    '--.':'g','....':'h','..':'i','.---':'j','-.-':'k','.-..':'l',
    '--':'m','-.':'n','---':'o','.--.':'p','--.-':'q','.-.':'r',
    '...':'s','-':'t','..-':'u','...-':'v','.--':'w','-..-':'x',
    '-.--':'y','--..':'z'
    }
    arr  = letter.split(" ")
    for i in arr :
        if i in morse :
            answer += morse[i]
    return answer

"""
000-62 ) A를 B로 만들기 
 https://school.programmers.co.kr/learn/courses/30/lessons/120886

"""
def solution(before, after):
    str1 = sorted(before)
    str2 = sorted(after)
    
    if str1 == str2 :
        return 1
    else :
        return 0

"""
000-63 ) 팩토리얼 
 https://school.programmers.co.kr/learn/courses/30/lessons/120848

"""
def solution(n):
    result = 1
    i = 1
    while result <= n :
        i += 1
        result *= i
        
    return i-1

"""
000-64 ) 2차원으로 만들기
 https://school.programmers.co.kr/learn/courses/30/lessons/120842

"""
def solution(num_list, n):
    answer = []
    
    while len(num_list) > 0 :
        arr = []
        for j in range(0,n) :
            arr.append(num_list[0])
            num_list.pop(0)
        answer.append(arr)
    return answer

"""
000-65 ) 가까운 수 
 https://school.programmers.co.kr/learn/courses/30/lessons/120890

    ** 차이가 같다면 더 작은 수를 리턴해야 하므로 정렬을 하고 시작함 
"""
def solution(array, n):
  answer = 0
  min = 9999
    
  array = sorted(array)

  for i in array :
    calNum = n - i

    if calNum < 0 :
      calNum *= -1


    if min > calNum :
      print("a")
      min = calNum
      answer = i
  return answer


"""
000-66 ) k의 개수 
 https://school.programmers.co.kr/learn/courses/30/lessons/120887

"""
def solution(i, j, k):
    answer = 0
    
    for i in range(i, j+1) :
        if str(k) in str(i) :
            answer += str(i).count(str(k))
    return answer

"""
000-67 ) 진료순서 정하기
 https://school.programmers.co.kr/learn/courses/30/lessons/120835

    0으로 초기화한 길이가 정해진 배열 선언 : [0 for i in range(n)]
    i가 위치한 index 값 리턴 : .index(i)
"""
def solution(emergency):
    answer = [0 for i in range(len(emergency))]
    cnt = 1
    arr = sorted(emergency, reverse = True)
    for i in arr :
        answer[emergency.index(i)] = cnt
        cnt += 1
    return answer

"""
000-68 ) 한번만 등장한 문자
 https://school.programmers.co.kr/learn/courses/30/lessons/120896

"""
def solution(s):
    answer = ''
    
    arr = list(s)
    for i in arr :
        if s.count(i) == 1 :
            answer += i
    
    return "".join(sorted(answer))

"""
000-69 ) 숨어있는 숫자의 덧셈 (2)
 https://school.programmers.co.kr/learn/courses/30/lessons/120864

    문자열에서 패턴에 해당하는 내용을 찾아 리스트로 반환 : re.findall(pattern, string)
    ** 1회 이상 반복되는 숫자들에 대한 패턴 : r'\d+'
"""
import re

def solution(my_string):
    numbers = re.findall(r'\d+', my_string)
    answer = 0
    for i in numbers :
        answer += int(i)
    
    return answer

"""
000-70 ) 이진수 더하기
 https://school.programmers.co.kr/learn/courses/30/lessons/120885

    2진수를 10진수로 변환 : int(2진수, 2)
    10진수를 2진수로 변환 : bin(10진수)
"""
def solution(bin1, bin2):
    return bin(int(bin1,2) + int(bin2,2))[2:]

"""
000-71 ) 7의 개수 
 https://school.programmers.co.kr/learn/courses/30/lessons/120912

    int형 리스트를 join하려면 map()을 이용해 str로 바꿔줘야 함 
"""
def solution(array):
    return "".join(map(str, array)).count("7")

"""
000-72 ) 잘라서 배열로 저장하기 
 https://school.programmers.co.kr/learn/courses/30/lessons/120913

"""
import math

def solution(my_str, n):
    answer = []
    start = 0
    end = n
    for i in range(0,math.ceil(len(my_str)/n)) :
        answer.append(my_str[start:end])
        start += n
        end += n
    return answer

"""
000-73 ) 다음에 올 숫자 
 https://school.programmers.co.kr/learn/courses/30/lessons/120924

"""
def solution(common):
    if common[1]-common[0] == common[2]-common[1] :
        # 등차수열 
        num = common[1]-common[0]
        return common[len(common)-1] + num
    else :
        # 등비 수열
        num = common[1]//common[0]
        return common[len(common)-1] * num

"""
000-74 ) 연속된 숫자의 합 
 https://school.programmers.co.kr/learn/courses/30/lessons/120923

"""
def solution(num, total):
    result = []
    
    midNum = total//num
    result.append(midNum) 
    
    if num % 2 == 0 :
        frontPos = (num-1)//2
        backPos = (num-1)-frontPos
        
        for i in range(1,frontPos+1) :
            result.insert(0,midNum-i)
            
        for i in range(1,backPos+1) :
            result.append(midNum+i)
                          
    else :
        position = (num-1)//2
        for i in range(1, position+1) :
            result.insert(0, midNum-i)
            result.append(midNum+i)
            
    return result

"""
000-75 ) 종이 자르기 
 https://school.programmers.co.kr/learn/courses/30/lessons/120922

"""
def solution(M, N):
    return M*N - 1


"""
000-76 ) OX 퀴즈
 https://school.programmers.co.kr/learn/courses/30/lessons/120907

"""   
def solution(quiz):
    aanswer = []
    for i in quiz :
      sen = i.split(" ")
      result = 0
      if sen[1] == "+" :
        result = int(sen[0]) + int(sen[2])

      if sen[1] == "-" :
        result = int(sen[0]) - int(sen[2])

      if result == int(sen[4]) :
          answer.append("O")
      else :
          answer.append("X")
    
    return answer

"""
000-77 ) 문자열 계산하기
 https://school.programmers.co.kr/learn/courses/30/lessons/120902

""" 
def solution(my_string):
    arr = my_string.split(" ")
    answer = int(arr[0])
    j = 1
    z = 2
    for i in range(1, ((len(arr)-1)//2)+1) :
        if arr[j] == "-" :
            answer -= int(arr[z])
    
        if arr[j] == "+" :
            answer += int(arr[z])   
            
        j += 2
        z += 2
    
    return answer      

"""
000-78 ) 영어가 싫어요
 https://school.programmers.co.kr/learn/courses/30/lessons/120894

"""
def solution(numbers):
    arrStrNum = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    arrNum = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    
    for i in range(0, 10) :
        numbers = numbers.replace(arrStrNum[i], str(arrNum[i]))

    return int(numbers)  