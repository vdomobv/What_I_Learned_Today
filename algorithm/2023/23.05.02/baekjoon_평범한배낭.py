import sys
input = sys.stdin.readline

"""
N : 물건 개수
W, V : 무게, 가치
K : 무게의 최대 값

풀이 접근 방법
1. 무게가 0부터 k까지 일때를 2차원 배열로 비교, 열 => 최대 무게, 행 => 물건의 값
2. 
    i: 최대 무게
    각 물건들이 i보다 작거나 같을 때, 이전 값과 비교해서 가치 최대값을 갱신해 준다.

"""

n, k = map(int, input().strip().split())
lst = [tuple(map(int, input().strip().split())) for _ in range(n)]

arr = [[0] * (k+1) for _ in range(n)]

for i in range(1, k+1):
    for j in range(n):
        w, v = lst[j][0], lst[j][1]
        if w > i:
            continue
        else:

            arr[j][i] = max(v + arr[j-1][i-w], arr[j-1][i])
# for i in range(n):
#     print(' '.join(list(map(str, arr[i]))))
print(arr[n-1][k])

"""
3 3
3 10
4 11
3 9

답 : 10
"""