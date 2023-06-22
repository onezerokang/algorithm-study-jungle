import sys
import heapq
input = sys.stdin.readline

def dijkstra(graph, start):
    # 거리를 무한대로 초기화
    distances = {node: float('inf') for node in graph}
    # 시작노드까지의 거리는 0으로 설정
    distances[start] = 0

    pq = []
    heapq.heappush(pq, (0, start))

    while pq:
        curr_dist, curr_node = heapq.heappop(pq)

        # 기존 거리보다 새로운 거리가 더 길면 무시
        if distances[curr_node] < curr_dist:
            continue
        
        for next_node, weight in graph[curr_node]:
            tmp_dist = curr_dist + weight
            if distances[next_node] > tmp_dist:
                distances[next_node] = tmp_dist
                heapq.heappush(pq, (tmp_dist, next_node))
    return distances

V, E = map(int, input().split())
start_node = int(input())
graph = {node: [] for node in range(1, V + 1)}
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

result = dijkstra(graph, start_node)
for x in result.values():
    print(x if x != float('inf') else "INF")