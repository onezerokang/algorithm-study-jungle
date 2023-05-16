# https://www.acmicpc.net/problem/10866
# logic
# push_front X: 정수 X를 덱의 앞에 넣는다.
# push_back X: 정수 X를 덱의 뒤에 넣는다.
# pop_front: 덱의 가장 앞에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# pop_back: 덱의 가장 뒤에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# size: 덱에 들어있는 정수의 개수를 출력한다.
# empty: 덱이 비어있으면 1을, 아니면 0을 출력한다.
# front: 덱의 가장 앞에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# back: 덱의 가장 뒤에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.

# push_front의 경우 배열복사를 하고 앞에 넣기

from sys import stdin
N = int(stdin.readline().strip())
cmds = [list(stdin.readline().strip().split()) for _ in range(N)]

def deque(c: list):
    ans = []
    for i in c:
        if i[0] == "push_front":
            ans = [i[1], *ans]
        elif i[0] == "push_back":
            ans.append(i[1])
        elif i[0] == 'pop_front':
            print(ans[0]) if len(ans) != 0 else print("-1")
            ans = ans[1:] if len(ans) != 0 else ans

        elif i[0] == 'pop_back':
            print(ans[-1]) if len(ans) != 0 else print("-1")
            ans.pop() if len(ans) != 0 else ans
        elif i[0] == 'size':
            print(len(ans))
        elif i[0] == 'empty':
            print("1") if len(ans) == 0 else print("0")
        elif i[0] == 'front':
            print("-1") if len(ans) == 0 else print(ans[0])
        elif i[0] == 'back':
            print("-1") if len(ans) == 0 else print(ans[-1])


deque(cmds)
