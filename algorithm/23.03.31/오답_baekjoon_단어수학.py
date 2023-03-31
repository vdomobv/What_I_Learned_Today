import sys
from collections import deque

n = int(sys.stdin.readline().strip())
arr = [list(sys.stdin.readline().strip()) for _ in range(n)]
arr.sort(key=len, reverse=True)

"""
반례
4
ABCD
BCDA
CDAB
DABG

답 : 33329
"""

# ==========================================================
"""
import sys
from collections import deque

n = int(sys.stdin.readline().strip())
arr = [deque(list(sys.stdin.readline().strip())) for _ in range(n)]

num = [i for i in range(10)]

# 길이가 긴 순서대로 배열을 정렬한다.
arr = sorted(arr, reverse=True)
arr = sorted(arr, key=len, reverse=True)
print(arr)
# print(arr)
alphabet = {}
result = ["" for _ in range(n)]

# 가장 큰 숫자부터 지정
k = 9

# 첫번째 문자열부터 시작
r = 0
flag = 0

while flag < n:
    # 첫번째 문자열의 길이가 뒤의 문자열보다 크거나 같다면 숫자를 배정 
    if arr[r]:
        if len(arr[r]) >= len(arr[(r+1)%n]):
            # 이미 알파벳의 숫자가 정해진 경우 다음 알파벳으로 이동
            if alphabet.get(arr[r][0]):
                t = arr[r].popleft()
                result[r] += alphabet[t]
            # 알파벳의 숫자가 정해지지 않은 경우 숫자 지정
            else:
                t = arr[r].popleft()
                alphabet[t] = str(k)
                result[r] += alphabet[t]
                k -= 1
        # 현재 문자열의 l번째의 길이가 뒤의 문자열보다 작다면 다음 문자열로 이동
        else:
            r = (r+1)%n
    else:
        flag += 1
        r = (r+1)%n

ans = 0
for r in result:
    ans += int(r)
print(result)
print(ans)
"""
# ==========================================================

# # 알파벳 문자열의 문자열의 맨 앞에서부터
# for i in arr:
#     tmp = ''
#     for j in i:
#         # 숫자가 배정되어 있다면 수를 추가한다.
#         if alphabet.get(j):
#             tmp += alphabet[j]
#         # 숫자가 배정되어 있지 않다면 큰 수부터 배정한다.
#         else:
#             alphabet[j] = str(k)
#             tmp += alphabet[j]
#             k -= 1
#     result += int(tmp)

# print(result)


"""
내 코드의 문제점 : 

ex)
ACDEB
GCF

오답 :
A = 9, C = 8, D = 7, E = 6, B = 5
              G = 4, C =  , F = 3

정답 : 
A = 9, C = 8, D = 7, E = 5, B = 4
              G = 6, C =  , F = 3
"""