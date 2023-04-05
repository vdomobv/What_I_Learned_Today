t = int(input())

for tc in range(1, t+1):
    n, m = map(int, input().split())
    
    arr = [list(map(int, input().split())) for _ in range(n)]
    ans = 0
    maxV = 0
    for k in range(1, n//2+1):
        expense = k*k+(k-1)*(k-1)
        for i in range(n):
            for j in range(n):
                cnt = 0
                for ti in range(arr[i][j] - k, arr[i][j] + k+1):
                    for tj in range(j - (k - abs(i-ti)), j + (k - abs(i-ti))+1):
                        if 0 <= ti < n and 0 <= tj < n and arr[ti][tj] == 1:
                            cnt += 1
                profit = cnt * m - expense
                if profit > maxV:
                    maxV = profit
                    ans = cnt
    
    print(f"#{tc} {ans}")