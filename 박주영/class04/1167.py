# 트리

# 트리의 지름을 구하시오

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)    

V = int(input().rstrip())
graph = [[] for _ in range(V+1)]

for _ in range(1, V+1):
    line = list(map(int, input().split()))
    idx = 0
    for j in range(len(line)-1):
        if j == 0:
            idx = line[j]
        elif j % 2 == 1:
            a = line[j]
            b = line[j+1]
            graph[idx].append([a, b])
        elif j % 2 == 0:
            continue

def dfs(x, weight):
    for i in graph[x]:
        a, b = i
        if distance[a] == -1:
            distance[a] = weight + b
            dfs(a, weight + b)
    return

# 첫번재 시행, 첫 요소부터 가장 먼 점 1찾는다

distance = [-1] * (V+1)
distance[1] = 0

dfs(1, 0)

start = distance.index(max(distance))

# 두번째 시행, 점 1부터 가장 먼 점 2를 찾는다, 이게 지름

distance = [-1] * (V+1)
distance[start] = 0

dfs(start, 0)

#========================

print(max(distance))