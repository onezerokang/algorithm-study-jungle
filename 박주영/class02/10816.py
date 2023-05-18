# 숫자 카드 2

# 숫자 카드는 정수 하나가 적혀져 있는 카드이다.
# 상근이는 숫자 카드 N개를 가지고 있다. 정수 M개가 주어졌을 때,
# 이 수가 적혀있는 숫자 카드를 상근이가 몇 개 가지고 있는지 구하는 프로그램을 작성하시오

# import sys
# input = sys.stdin.readline

# N = int(input().rstrip()) # 상근이가 가지고 있는숫자 카드의 개수
# Cards = list(map(int, input().split())) # 숫자 카드에 적혀있는 정수
# M = int(input().rstrip()) # M, 주어진 정수
# Nums = list(map(int, input().split())) # 상근이가 가지고 있는 카드 중 구해야 할 카드

# # print(N)
# # print(Cards)
# # print(M)
# # print(Nums)     
# # cards 중에서 nums에 적혀있는 경우 가지고 있는 카드의 수가 몇 개인지 출력해야 한다.


# def findlist(cards, nums, n, m):
#     count = [0] * m
#     # print(count)
#     for i in range(len(cards)):
#         for j in range(len(nums)):
#             if cards[i] == nums[j]:
#                 count[j] += 1
#     for k in range(len(count)):
#         print(count[k], end=' ')

# findlist(Cards, Nums, N, M)

# 시간초과

# 이진 탐색 , 해시 맵: 파이썬의 딕셔너리는 해시테이블

import sys
input = sys.stdin.readline

N = int(input().rstrip()) # 상근이가 가지고 있는숫자 카드의 개수
Cards = sorted(list(map(int, input().split()))) # 숫자 카드에 적혀있는 정수
M = int(input().rstrip()) # M, 주어진 정수
Nums = list(map(int, input().split())) # 상근이가 가지고 있는 카드 중 구해야 할 카드

count = {} # 카드 세기
for card in Cards:
    if card in count:
        count[card] += 1
    else:
        count[card] = 1

def bs(arr, target, start, end):
    if start > end:
        return 0
    mid = (start + end) // 2
    if target > arr[mid]:
        return bs(arr, target, mid+1, end)
    elif target < arr[mid]:
        return bs(arr, target, start, mid-1)
    else:
        return count.get(target) # 타겟을 찾았다면 딕셔너리에서 갯수 찾아 반환


for k in Nums:
    print(bs(Cards, k, 0, len(Cards)-1), end=' ')

