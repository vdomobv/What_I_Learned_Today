def solution(s):
    answer = len(s)
    
    l = len(s)
    
    for i in range(1, l//2+1):
        tmp = ""
        last = 0
        stack = []
        for j in range(0, l, i):
            if j+i <= len(s):
                a = s[j:j+i]
                if len(stack) == 0:
                    stack.append(a)
                elif a == stack[-1]:
                    stack.append(a)
                else:
                    sl = len(stack)
                    if sl > 1:
                        tmp += str(sl)
                    p = stack.pop()
                    tmp += p
                    stack = [a]
            else:
                last = j

        if stack:
            if len(stack) > 1:
                tmp += str(len(stack))
            p = stack.pop()
            tmp += p
            
        if last:
            tmp += s[last:]
            
        answer = min(answer, len(tmp))
    return answer