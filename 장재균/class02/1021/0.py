import sys
input = sys.stdin.readline
from collections import deque

queue = deque
count = 0
N, M = map(int, input().split())

queue = [i for i in range(1, N + 1)]
s = list(map(int ,input().split()))
count = 0
for i in range(M):
    q_len = len(queue)
    q_index = queue.index(s[i])
    if q_index < q_len - q_index:
        while True:
            if queue[0] == s[i]:
                del queue[0]
                break
            else:
                queue.append(queue[0])
                del queue[0]
                count += 1
    else:
        while True:
            if queue[0] == s[i]:
                del queue[0]
                break
            else:
                queue.insert(0, queue[-1])
                del queue[-1]
                count += 1
print(count)