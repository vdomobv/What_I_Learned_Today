import sys
input = sys.stdin.readline

"""
N : 물건 개수
W, V : 무게, 가치
K : 무게의 최대 값

풀이 접근 방법
1. 물품을 무게로 정렬한다.
2. 
"""

N, K = map(int, input().strip().split())
lst = [tuple(map(int, input().strip().split())) for _ in range(N)]
lst.sort()
