# 1 : 방안의 사람들
# 나머지 : 계단의 입구

t = int(input())

for tc in range(1, t+1):
    n = int(input())

    arr = []
    stairs = []
    people = []
    # 배열 입력
    for i in range(n):
        t = list(map(int, input().split()))
        arr.append(t)

        for j in range(n):
            # 사람 위치 확인
            if t[j] == 1:
                people.append((i, j))
            # 계단위치 확인
            elif t[j] > 1:
                stairs.append((i, j))
    

"""
접근방법 : 
1. 사람들을 두그룹으로 나눈다 from itertools import combinations
2. 그룹 별로 각 사람들이 계단까지 도착하는 시간을 구한다.
3. 시간 +1 을 반복하며 
"""
    