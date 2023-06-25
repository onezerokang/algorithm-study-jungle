import sys
input = sys.stdin.readline

INF = int(1e9)
sys.setrecursionlimit(INF)

n = int(input())
d = [0] * (n + 1)

def fibo(x):
    if x == 1 or x == 2:
        return 1

    if d[x] != 0:
        return d[x]

    d[x] = fibo(x - 1) + fibo(x - 2)
    return d[x]

if n == 0:
    print(0)
else:
    print(fibo(n) % 1000000007)
