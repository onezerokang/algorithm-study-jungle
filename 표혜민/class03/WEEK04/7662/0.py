# https://www.acmicpc.net/problem/7662
# logic
import heapq
from sys import stdin
T = int(stdin.readline().strip())
for _ in range(T):
    k = int(stdin.readline().strip())
    q,rev_q = [],[]
    # idx = 0
    for i in range(k):
        inst = stdin.readline().strip().split()
        if inst[0] == 'I':
            heapq.heappush(q, int(inst[1]))
            heapq.heappush(rev_q, int(inst[1]))
        if inst[0] == 'D' and q: 
            if inst[1] == '-1': #최소값 제거
                heapq.heappop(q)
            elif inst[1] == '1': #최대값 제거
                rev_q.reverse()
                rev_q.pop()
                print("q", q)
                heapq.heapify([*rev_q])
                print("rev_q", rev_q)
                # print("rev_q", rev_q)
    print("q", q)
    print("EMPTY") if len(q) == 0 else print(q[-1], q[0])
