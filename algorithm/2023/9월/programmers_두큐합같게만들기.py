from collections import deque

def solution(queue1, queue2):
    temp = queue1 + queue2
    temp = sorted(temp)
    
    total = sum(temp)
    half = total/2
    
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    
    answer = 0
    
    q1_sum = sum(queue1)
    q2_sum = sum(queue2)
    
    if half % 1:
        return -1
    
    if sum(temp) - max(temp) < max(temp):
        return -1
    
    while q1_sum != q2_sum:
        if q1_sum > half and queue1:
            t = queue1.popleft()
            queue2.append(t)
            q1_sum -= t
            q2_sum += t 

        elif q2_sum > half and queue2:
            t = queue2.popleft()
            queue1.append(t)
            q2_sum -= t
            q1_sum += t
        else:
            return -1
        
        answer += 1
        
        if answer >= 600000:
            return -1
        
    
    return answer