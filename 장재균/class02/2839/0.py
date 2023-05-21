import sys
input = sys.stdin.readline

n = int(input())

count = 0
# while True:
#     if n >= 5:
#         count += n // 5
#         n = n % 5
#     elif n < 5 and n >= 3:
#         count += n // 3
#         n = n % 3
#     elif n == 0:
#         print(count)
#         break
#     else:
#         print(-1)
#         break

while True:
    if n % 5 != 0:
        n -= 3
        count += 1
    elif n * 5 == 0:
        count += n % 5
        print(count)
        break
    elif n < 0:
        print(-1)
        break
