"""
풀이 접근 방법
i번째 행 j번째 열 위치로 올 수 있는 길은
    0번째 일경우, arr[i-1][0]
    i번째일 경우, arr[i-1][j-1]
    나머지는 두 가지 경우중 가장 큰 값을 만드는 경우
"""

import sys
input = sys.stdin.readline

n = int(input().strip())
arr = [list(map(int, input().strip().split())) for _ in range(n)]

for i in range(1, n):
    for j in range(i+1):
        if j == 0:
            arr[i][j] += arr[i-1][0]
        elif j == i:
            arr[i][j] += arr[i-1][j-1]
        else:
            arr[i][j] += max(arr[i-1][j-1], arr[i-1][j])

print(max(arr[n-1]))