def solution(s):
    lst = []
    
    for i in s:
        if i=="(":
            lst.append(i)
        else:
            if lst:
                lst.pop()
            else:
                return False
            
    if lst:
        return False
    
    return True