def solution(s):
    answer = []
    
    s = s.split("},{")
    for i in range(len(s)):
        s[i] = s[i].replace("{","").replace("}","")
    
    s = sorted(s, key = lambda x : len(x))

    for i in s:
        t = list(map(int, i.split(",")))
        answer.extend([x for x in t if x not in answer])
        
    return answer