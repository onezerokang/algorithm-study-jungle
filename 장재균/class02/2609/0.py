# 최대공약수의 범위 : 1부터 둘 중 작은 숫자까지
# 최소공배수의 범위 : 둘 중 큰 숫자부터 두 수의 곱한 값 까지

import sys
import math
input = sys.stdin.readline

N, M = map(int, input().split())
# if N > M:
#     max = N
#     min = M
# else:
#     max = M
#     min = N

# for i in range(min+1, 0, -1):
#     if N % i == 0 and M % i == 0:
#         print(i)
#         break

# for i in range(max, (N * M)+1):
#     if i % N == 0 and i % M == 0:
#         print(i)
#         break

# 시간 초과, 유클리드 호제법

def gcd(N, M):
    while M > 0:
        N, M = M, N % M
    return N

def lcm(N, M):
    return N * M / gcd(N, M)

print(gcd(N, M))
print(round(lcm(N, M)))