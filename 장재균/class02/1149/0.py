import sys
input = sys.stdin.readline

N = int(input())

num = []
for _ in range(N):
    num.append(list(map(int, input().split())))

for i in range(1, len(num)):
    num[i][0] = min(num[i - 1][1], num[i - 1][2]) + num[i][0]
    num[i][1] = min(num[i - 1][0], num[i - 1][2]) + num[i][1]
    num[i][2] = min(num[i - 1][0], num[i - 1][1]) + num[i][2]

print(min(num[N - 1][0], num[N - 1][1], num[N - 1][2]))
