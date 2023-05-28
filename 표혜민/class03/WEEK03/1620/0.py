# https://www.acmicpc.net/problem/1620
import sys
input = sys.stdin.readline
N, M = map(int, input().split())  # 1<=N,M<=100000
p1, p2 = dict(), dict()
for i in range(1, N + 1):
    pkm = input().rstrip()
    p1[str(i)] = pkm
    p2[pkm] = str(i)

for _ in range(M):
    q = input().rstrip()
    print(p1[q]) if q.isdigit() else print(p2[q])
