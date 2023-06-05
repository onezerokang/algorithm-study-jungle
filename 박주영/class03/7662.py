# 이중 우선순위 큐 dual priority queue

# 전형적인 우선순위 큐처럼 데이터를 삽입, 삭제할 수 있는 자료 구조이다.
# 큐와의 차이점은 데이터를 삭제할 때 연산(operation) 명령에 따라 우선순위가 가장 높은 
# 데이터 또는 가장 낮은 데이터 중 하나를 삭제하는 점이다.
#  두 가지 연산이 사용되는데, 하나는 데이터를 삽입하는 연산이고 다른 하나는
# 데이터를 삭제하는 연산이다. 데이터를 삭제하는 연산은 또 두 가지로 구분되는데
# 하나는 우선순위가 가장 높은 것을 삭제하기 위한 것이고 다른 하나는 우선순위가 
# 가장 낮은 것을 삭제하기 위한 것이다. 

# import sys
# from collections import deque
# input = sys.stdin.readline

# 명령을 처리하는 함수, 이중 우선순위 큐를 처리한다.
# 만약 큐가 우선순위대로 정렬되어 있다면, 삭제할 때에는 순서 고려 없이 첫, 마지막만 빼내면 된다.

# heapify가 있는데 왜 사용을 안하니!!!!!!!!!!!!!1

# def dpq(order,arr):
#     # order은 2개의 첫째 줄 index에 명령, 둘째 index엔 연산할 숫자를 가짐(string)
#     # arr은 deque
#     if order[0] == 'I':
#         queue(arr)
#         arr.append(order[1])
#         arr.sort() #O(nlogn)의 시간복잡도를 가짐, timsort 방법을 사용한다.
#         #dequeu는 sort를 지원하지 않는다.
#     elif order[0] == 'D':
#         deque(arr)
#         if order[1] == '1':
#             arr.leftpop()
#         elif order[1] == '-1':
#             arr.pop()

# arr = deque()
# T = int(input().rstrip())
# for _ in range(T):
#     num = int(input().rstrip())
#     test = deque()
#     for _ in range(num):
#         cmd = list(map(str, input().split()))
#         dpq(cmd, test)
#     if (len(test) == 0):
#         print('EMPTY')
#     else:
#         print(test[0], test[-1])
# 

# heap // 결국 풀이를 봤지만.

import sys
import heapq
input = sys.stdin.readline

def worker(num):
    ascend = []
    descend = []
    deleted = [True]*num
    for i in range(num):
        cmd, n = input().split()
        n = int(n)
        if cmd == 'I':
            heapq.heappush(ascend, (-n, i)) # 첫 원소의 값은 ascend[0][0], 삭제 여부는 ascend[0][1]
            heapq.heappush(descend, (n, i)) # 나머지는 힙으로는 다룰 수 없으니 나오는 건 위 두개 뿐
            deleted[i] = False
        else:
            if n == 1:
                while ascend and deleted[ascend[0][1]]: # 이미 삭제됐다면 팝해버림
                    heapq.heappop(ascend)
                if ascend:
                    deleted[ascend[0][1]] = True
                    heapq.heappop(ascend)
            else:
                while descend and deleted[descend[0][1]]:
                    heapq.heappop(descend)
                if descend:
                    deleted[descend[0][1]] = True
                    heapq.heappop(descend)

    while ascend and deleted[ascend[0][1]]:
        heapq.heappop(ascend)
    while descend and deleted[descend[0][1]]:
        heapq.heappop(descend)

    if ascend and descend: #원소가 존재하면 True를 반환###
        print(-ascend[0][0], descend[0][0])
    else:
        print('EMPTY')

T = int(input().rstrip()) # test case 수
for _ in range(T):
    num = int(input().rstrip()) #command 수
    worker(num)
    
