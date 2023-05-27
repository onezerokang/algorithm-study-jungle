# 숨바꼭질

# 1 차원 좌표에 있는 수빈이와 동생은 숨바꼭질을 하고 있다:
# 수빈이는 위치가 X일 때 X-1, X+1, 순간이동 할 경우에는 2*X의 위치로 이동한다.
# 둘의 위치가 주워질 때, 수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후인지 구하시오

import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())
# N = 수빈이가 있는 위치 K = 동생이 있는 위치
# 최소 조작 횟수를 찾으므로 bfs를 생각할 수 있다.

MAX = 100001
array = [0]*MAX # 여기까지 오는 횟수

def hideNseek(n):
    q = deque([n]) 
    while (q):
        n = q.popleft()
        if n == K:
            return array[n]
        for next_n in (n-1, n+1, 2*n): # 이렇게도 쓸 수 있군
            if 0 <= next_n < MAX and not array[next_n]: #큐에 있다면 최소 값에서 움직여야 한다
                array[next_n] = array[n] +1
                q.append(next_n)
print(hideNseek(N))
