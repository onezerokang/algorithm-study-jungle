# import sys
# input = sys.stdin.readline

# n = int(input())
# s = set()
# for i in range(n):
#     cmd = input().split()
#     if cmd[0] == "add":
#         s.add(cmd[1])
#     elif cmd[0] == "remove":
#         if cmd[1].isdigit() and cmd[1] in s:
#             s.remove(cmd[1])
#         else:
#             continue
#     elif cmd[0] == "check":
#         if cmd[1].isdigit() and cmd[1] in s:
#             print(1)
#         else:
#             print(0)
#     elif cmd[0] == "toggle":
#         if cmd[1].isdigit():
#             if cmd[1] in s:
#                 s.remove(cmd[1])
#             else:
#                 s.add(cmd[1])
#         else:
#             continue
#     elif cmd[0] == "all":
#         s = set(str(i) for i in range(1, 21))
#     elif cmd[0] == "empty":
#         s = set()

# 시간 초과

import sys
input = sys.stdin.readline

m = int(sys.stdin.readline())
S = set()

for _ in range(m):
    temp = sys.stdin.readline().strip().split()
    
    if len(temp) == 1:
        if temp[0] == "all":
            S = set([i for i in range(1, 21)])
        else:
            S = set()
    
    else:
        func, x = temp[0], temp[1]
        x = int(x)

        if func == "add":
            S.add(x)
        elif func == "remove":
            S.discard(x)
        elif func == "check":
            print(1 if x in S else 0)
        elif func == "toggle":
            if x in S:
                S.discard(x)
            else:
                S.add(x)

# add, remove, check, toggle은 x라는 파라미터가 필요하지만 all과 empty는 그렇지 않다.

# 그럼으로 처음 입력값을 받는 temp의 길이로 x가 존재 유무를 파악해서 x가 없다면

# all과 empty일 때로 나누어서 집합을 만들어 줌

# x가 존재할 때는 int형으로 바꿔주어서 사용

# 이 때 remove대신에 discard함수를 사용한건 remove함수는 존재하지 않는 수를 제거하려고 하면

# 오류를 발생하는데 discard함수를 사용하면 오류가 나지않고 정상종료할 수 있다.

# 주어진 연산의 수를 다 수행하면 반복문이 종료된다