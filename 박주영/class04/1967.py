# 트리의 지름

# 트리의 지름을 구하는 다른 문제이다.
# 임의 점에서 가장 먼 점 , 거기서 먼 점을 구한다.
# dfs와 bfs로 풀 수 있으나 복습이 필요한 dfs로 풀어보자.

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def dfs(Start, Graph, Distance):
    for i in Graph[Start]:
        next_node, weight = i
        if (Distance[next_node] == -1):
            Distance[next_node] = weight + Distance[Start]
            dfs(next_node, Graph, Distance)

n = int(input().rstrip())
graph = [[]*(n+1) for _ in range(n+1)]

for i in range(n-1):
    parent, child, weight = map(int, input().split())
    graph[parent].append([child, weight])
    graph[child].append([parent, weight])

distance_rand = [-1] * (n+1)
distance_rand[1] = 0
dfs(1, graph, distance_rand)
point1 = distance_rand.index(max(distance_rand))

distance_radius = [-1] * (n+1)
distance_radius[point1] = 0
dfs(point1, graph, distance_radius)
ans = max(distance_radius)

print(ans)