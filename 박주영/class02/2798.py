# N장의 카드에 써져 있는 숫자가 주어졌을 때, 
# M을 넘지 않으면서 M에 최대한 가까운 카드 3장의 합을 구해 출력하시오.

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
cards = list(map(int, input().split()))

def blackjack(N, M, array):
    summation = 0
    for i in range(N):
        if array[i] > M:
            continue
        for j in range(i+1, N):
            if array[i]+array[j] > M:
                continue
            for k in range(j+1, N):
                if array[i] + array[j] + array[k] > M:
                    continue
                newSum = array[i]+array[j]+array[k]
                if ((M - summation) > (M - newSum)):
                    summation = newSum
    print(summation)

blackjack(n, m, cards)