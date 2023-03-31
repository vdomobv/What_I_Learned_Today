import sys

t = int(sys.stdin.readline().strip())

for _ in range(t):
    n = int(sys.stdin.readline().strip())
    arr = []

    for i in range(n):
        arr.append(tuple(map(int, sys.stdin.readline().strip().split())))

    arr.sort(reverse=True)

    cnt = n
    for i in range(n-1):
        for j in range(i+1, n):
            if arr[i][1] > arr[j][1]:
                cnt -= 1
                break
    
    print(cnt)