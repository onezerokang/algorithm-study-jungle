# from heapq import nlargest, nsmallest, heappush, heappop
# from sys import stdin
# T = int(stdin.readline().strip())
# for _ in range(T):
#     k = int(stdin.readline().strip())
#     min_h, max_h = [], []
#     for i in range(k):
#         inst, num = stdin.readline().strip().split()
#         num = int(num)
#         if inst == 'I':
#             heappush(min_h, num)
#             heappush(max_h, -num)
#         else:
#             if min_h and num == -1:
#                 heappop(min_h)
#             if max_h and num == 1:
#                 heappop(max_h)

#     if len(max_h) == 0 or len(min_h) == 0:
#         print("EMPTY")
#     else:

#         min_h1 = nsmallest(1, min_h)[-1]
#         max_h1 = -(nsmallest(1, max_h)[-1])
#         print(max_h1, min_h1) if max_h1 != min_h1 else print("EMPTY")
# 22%에서 틀렸습니다 ㅜㅜ
