def solution(s):
    answer = []
    
    lst = s[1:-1].split("},{")
    for i in range(len(lst)):
        lst[i] = lst[i].strip("{}")
    lst.sort(key=lambda x:len(x))
    
    for l in lst:
        tmp = list(map(int, l.split(",")))
        for t in tmp:
            if t not in answer:
                answer.append(t)

    return answer