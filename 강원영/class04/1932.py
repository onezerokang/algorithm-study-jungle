import sys
input = sys.stdin.readline

N = int(input())
a = [list(map(int, input().split())) for _ in range(N)]

for i in range(N - 2, -1, -1):
    for j in range(i + 1):
        a[i][j] += max(a[i + 1][j], a[i + 1][j + 1])

print(a[0][0])