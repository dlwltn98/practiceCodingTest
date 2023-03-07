"""
001 ) 옹알이 (1)
 https://school.programmers.co.kr/learn/courses/30/lessons/120956

"""
def solution(babbling):
    answer = 0
    
    # 할 수 있는 단어 저장
    words = ["aya", "ye", "woo", "ma"]
    
    for i in babbling :
        wordCopy = i
        
        for j in words :
            if len(wordCopy) > 0 :
                wordCopy = wordCopy.replace(j, " ")

            if len(wordCopy.replace(" ", "")) == 0 :
                answer += 1
                break 
    
    return answer

"""
001-1 ) 자릿수 더하기
 https://school.programmers.co.kr/learn/courses/30/lessons/12931

"""
def solution(n):
    arr = list(map(int, str(n)))
    
    result = 0
    for i in arr :
        result += i
        
    return result