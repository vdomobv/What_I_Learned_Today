import sys

n, s = map(int, sys.stdin.readline().strip().split())
arr = list(map(int, sys.stdin.readline().strip().split()))

def solve(i, val_list):
    global ans
    if i == n:
        return
    
    if sum(val_list) == s:
        ans += 1
    
    val_list.append(arr[i])
    solve(i+1, val_list)
    val_list.pop()

ans = 0
solve(0, [])
print(ans)
