def solution(rows, columns, queries):
    answer = []
    
    arr = [[0]*columns for _ in range(rows)]
    k = 1
    for i in range(rows):            
        for j in range(columns):
            arr[i][j] = k
            k+=1
    
    for x1, y1, x2, y2 in queries:
        x, y = x1 - 1, y1 - 1
        n = arr[x][y]
        m = arr[x][y]
        
        while y < y2-1:
            t = arr[x][y+1]
            arr[x][y+1] = n
            if n < m:
                m = n
            n = t
            y += 1
            
        while x < x2-1:
            t = arr[x+1][y]
            arr[x+1][y]= n
            if n < m:
                m = n
            n = t
            x += 1
                
        while y1-1 < y:
            t = arr[x][y-1]
            arr[x][y-1]= n
            if n < m:
                m = n
            n = t
            y -= 1
        
        while x1-1 < x:
            t = arr[x-1][y]
            arr[x-1][y]= n
            if n < m:
                m = n
            n = t
            x -= 1
        
        answer.append(m)
        
    return answer