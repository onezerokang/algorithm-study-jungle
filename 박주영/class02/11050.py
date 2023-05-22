# 이항 계수1Binomial coefficient: 다항식을 전개하였을 때 각 요소의 계수

# 자연수 N과 정수 K가 주어졌을 때 이항 계수 (N K)를 구하는 프로그램을 작성하시오.

import sys
input = sys.stdin.readline

N, K = map(int, input().split())

def BinomCoe(n, k):
    ans = 1
    for i in range(k+1, n+1):
        ans *= i
    for j in range(1, n-k+1):
        ans /= j 
    print(int(ans))

BinomCoe(N, K)