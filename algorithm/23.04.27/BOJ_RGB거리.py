"""
풀이 접근 방법
1. 양옆으로 같은 색만 아니면 괜찮다.
2. 차례로 색을 정하기 때문에 현재 위치의 색을 정하고 앞전까지의 최소값을 찾아서 더해준다.
    => 구하고자 하는 것은 각각 집에 어떤 색인지가 아니라 최소값,
    => 선택 기준 포인트를 다른 두 색 중에 무엇이냐 보다
        색이 같지 않은 것중에 어떤 색이 더 최소값이냐로 둘것!
"""

import sys
input = sys.stdin.readline

n = int(input().strip())
arr = [list(map(int, input().strip().split())) for _ in range(n)]
for i in range(1, n):
    arr[i][0] += min(arr[i-1][1], arr[i-1][2])
    arr[i][1] += min(arr[i-1][0], arr[i-1][2])
    arr[i][2] += min(arr[i-1][1], arr[i-1][0])

print(min(arr[n-1]))