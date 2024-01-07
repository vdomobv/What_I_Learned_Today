def solution(n):
    answer = 0
    
    temp = ""
    while n > 2:
        temp += str(n%3)
        n //= 3
    temp += str(n)
    
    l = len(temp)
    for i in range(l):
        answer += (3**i)*int(temp[l-1-i])
    
    return answer