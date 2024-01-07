def solution(s, n):
    answer = ''
    for i in s:
        if i.islower():
            t = ord(i) + n if ord(i) + n <= 122 else ord(i) + n - 26
        elif i.isupper():
            t = ord(i) + n if ord(i) + n <= 90 else ord(i) + n - 26
        else:
            answer += i
            continue

        answer += chr(t)
    return answer