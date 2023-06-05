from collections import deque
t = int(input())

for tc in range(1, t+1):
    n, m = map(int, input().split())
    lst = [set() for _ in range(n+1)]
    for _ in range(m):
        a, b = map(int, input().split())
        lst[a].add(b)
        lst[b].add(a)

    check = [0] * (n+1)
    cnt = 0
    q=deque([])
    for i in range(1, n+1):
        if check[i]==0:
            cnt += 1
            q.append(i)
            check[i] = 1
            while q:
                t = q.popleft()
                for j in lst[t]:
                    if check[j]==0:
                        check[j] = 1
                        q.append(j)
    
    print(f"#{tc} {cnt}")
