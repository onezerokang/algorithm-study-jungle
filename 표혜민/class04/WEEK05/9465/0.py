#1932랑 비슷한 문제
import sys
input = sys.stdin.readline
T = int(input().rstrip())
ans = []
for _ in range(T):
    N = int(input())    #(1 ≤ n ≤ 100,000)
    stk = [list(map(int, input().split())) for _ in range(2)]
    for i in range(1,N):
        if i == 1:
            stk[0][i] += stk[1][i-1]
            stk[1][i] += stk[0][i-1]
        else:
            stk[0][i] += max(stk[1][i-1],stk[1][i-2])
            stk[1][i] += max(stk[0][i-1],stk[0][i-2])

    print(max(stk[0][N-1],stk[1][N-1]))