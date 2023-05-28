# 정수를 저장하는 덱(Deque)를 구현한 다음
# 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.

# push_front / push_back / pop_front / pop_back / 
# size / empty / front / back

# 사실, C++로 작성하면 양이 많아지고 할 것도 많을 것 같긴 합니다만...
# 그냥 파이썬 deque썼습니다....
# 시간 남으면 C++로 해볼게요...

import sys
from collections import deque
input = sys.stdin.readline

testcase = int(input())
q = deque()
def deque_test (x):
    if(x[0] == 'push_front'): #left를 end로, right를 front로.
        q.append(int(x[1]))
    elif(x[0] == 'push_back'):
        q.appendleft(int(x[1]))
    elif(x[0] == 'pop_front'):
        if (len(q) == 0):
            print(-1)
        else:
            print(q.pop())
    elif(x[0] == 'pop_back'):
        if (len(q) == 0):
            print(-1)
        else:
            print(q.popleft())
    elif(x[0] == 'size'):
        print(len(q))
    elif(x[0] == 'empty'):
        if(len(q) == 0):
            print(1)
        else:
            print(0)
    elif(x[0] == 'front'):
        if (len(q) == 0):
            print(-1)
        else:
            print(q[-1])
    elif(x[0] == 'back'):
        if (len(q) == 0):
            print(-1)
        else:
            print(q[0])
    return

for _ in range(testcase):
    order = list(map(str, input().rstrip().split()))
    deque_test(order)
