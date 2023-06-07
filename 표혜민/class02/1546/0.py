from sys import stdin
N = int(stdin.readline().strip())
scr = list(map(int, stdin.readline().strip().split()))
M = max(scr)
print(sum(list(map(lambda i: i/M*100, scr)))/N)
