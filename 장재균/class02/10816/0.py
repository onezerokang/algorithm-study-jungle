# import sys
# input = sys.stdin.readline

# N = int(input())

# card_list = list(map(int, input().split()))

# M = int(input())

# check_list = list(map(int, input().split()))

# anw= []
# for i in range(M):
#     anw.append(card_list.count(check_list[i]))

# print(*anw)

import sys
from collections import Counter

# 입력 받기
N = int(sys.stdin.readline())
card_list = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
chack_list = list(map(int, sys.stdin.readline().split()))

# 카드 숫자 개수 세기
card_counter = Counter(card_list)

# 결과 출력
for num in chack_list:
    print(card_counter[num], end=" ")