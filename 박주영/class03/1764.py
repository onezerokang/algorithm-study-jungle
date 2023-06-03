# 듣보잡
# 김진영이 듣도 못한 사람의 명단과, 보도 못한 사람의 명단이 주어질 때,
# 듣도 보도 못한 사람의 명단을 구하는 프로그램을 작성하시오.

import sys
input = sys.stdin.readline

N, M = map(int, input().split())

notHeard = {}
listofnobody = [] * 500000
for i in range(N):
    notHeard[input().rstrip()] = 'notHeard'
for j in range(M):
    cnd = input().rstrip()
    # print(cnd)
    if(cnd in notHeard):
        listofnobody.append(cnd)
        # print('finding', listofnobody)
listofnobody.sort()
print(len(listofnobody))
for i in range(len(listofnobody)):
    print(listofnobody[i])