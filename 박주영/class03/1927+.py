# 최소 힙

# 배열에 자연수 x를 넣는다
# 배열에서 가장 작은 값을 출력하고 그 값을 제거한다

import sys
from heapq import heappop, heappush
input = sys.stdin.readline

h = []

N = int(input().rstrip())

for _ in range(N):
    cmd = input().rstrip()
    if cmd == '0':
        if len(h) == 0:
            print(0)
            continue
        print(heappop(h))
    else:
        num = int(cmd)
        heappush(h, num)
