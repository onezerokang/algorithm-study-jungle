# import sys
# input = sys.stdin.readline

# T = int(input())

# for _ in range(T):
#     Q = int(input())
#     queue = []
#     for j in range(Q):
#         num = input().rsplit()
#         if num[0] == "I":
#             queue.append(int(num[1]))
#             queue.sort()
#         elif num[0] == "D":
#             if num[1] == "1":
#                 if queue == []:
#                     continue
#                 else:
#                     del queue[-1]
#             elif num[1] == "-1":
#                 if queue == []:
#                     continue
#                 else:
#                     del queue[0]
    
#     if queue == []:
#         print("EMPTY")
#     else:
#         print(queue[-1], queue[0])

# 시간 초과

import sys
import heapq
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    Q = int(input())
    max_heapq = []
    min_heapq = []
    visited = [False] * Q
    for i in range(Q):
        N, M = input().split()
        M = int(M)
        if N == "I":
            heapq.heappush(min_heapq, (M, i))
            heapq.heappush(max_heapq, (-M, i))
            visited[i] = True
        elif M == 1:
            while max_heapq and not visited[max_heapq[0][1]]:
                heapq.heappop(max_heapq)
            if max_heapq:
                visited[max_heapq[0][1]] = False
                heapq.heappop(max_heapq)
        else:
            while min_heapq and not visited[min_heapq[0][1]]:
                heapq.heappop(min_heapq)
            if min_heapq:
                visited[min_heapq[0][1]] = False
                heapq.heappop(min_heapq)
    while min_heapq and not visited[min_heapq[0][1]]:
        heapq.heappop(min_heapq)
    while max_heapq and not visited[max_heapq[0][1]]:
        heapq.heappop(max_heapq)
    print(-max_heapq[0][0], min_heapq[0][0]) if max_heapq and min_heapq else print("EMPTY")