import sys
input = sys.stdin.readline

N = int(input())
times = list(map(int, input().split()))
times.sort()

ans = [0] * N
ans[0] = times[0]

for i in range(1, N):
    ans[i] = ans[i - 1] + times[i]

print(sum(ans))