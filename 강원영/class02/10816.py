import sys
input = sys.stdin.readline

N = int(input())
cards = list(map(int, input().split()))
M = int(input())
count_cards = (list(map(int, input().split())))

answer = {}
for card in count_cards:
    answer[card] = 0

for card in cards:
    if card in answer:
        answer[card] += 1

for card in count_cards:
    print(answer[card], end = ' ')