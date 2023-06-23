import sys
import heapq

V, E = map(int, input().split())
K = int(input())

graph = [{} for _ in range(V+1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    if v in graph[u]:
        graph[u][v] = max(graph[u][v], w)
    else:
        graph[u][v] = w

def dijkstra(graph, start):
    distances = {node: float('inf') for node in range(1, V+1)}
    distances[start] = 0
    queue = []
    heapq.heappush(queue, [distances[start], start])

    while queue:
        dist, node = heapq.heappop(queue)

        if distances[node] < dist:
            continue

        for next_node, next_dist in graph[node].items():
            distance = dist + next_dist
            if distance < distances[next_node]:
                distances[next_node] = distance
                heapq.heappush(queue, [distance, next_node])
    return distances

distances = dijkstra(graph, K)
for i in distances.values():
    if i == float('inf'):
        print('INF')
    else:
        print(i)
