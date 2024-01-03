def solution(n):
    arr = [[0] * (i+1) for i in range(n)]
    
    i, j = -1, 0
    lst = [[1,0], [0,1], [-1,-1]]
    d=0
    last = sum(list(k for k in range(1, n+1)))
    
    cnt = 1
    while cnt <= last:
        
        for _ in range(n):
            i += lst[d][0]
            j += lst[d][1]
            arr[i][j] = cnt
            cnt += 1
            
        n-=1
        if d < 2:
            d+=1
        else:
            d=0
            
    answer = sum(arr, [])
    return answer