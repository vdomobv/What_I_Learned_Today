def solution(s):
    answer = ''
    t = 1
    i = 0
    while i < len(s):
        if s[i].isspace():
            answer += " "
            t = 1
        else:
            answer += s[i].upper() if t == 1 else s[i].lower()
            t *= -1
        i += 1
    return answer