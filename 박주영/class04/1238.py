# 파티
# 다익스트라

import sys, heapq # min heap
input = sys.stdin.readline
INF = int(1e9)

def dijkstra(Start, list):
    distance = [INF] * (N+1)
    heap = []
    heapq.heappush(heap, [0, Start]) # START지점에서 시작
    distance[Start] = 0 # 시작 지점으로부터 걸리는 거리들을 저장

    while heap:

        cost_now, node = heapq.heappop(heap) # 현재 위치를 뽑아서
        for cost_next, node_next in list[node]: # 리스트를 돌면서
            cost_next += cost_now # 현재까지의 코스트에 다음 거리까지를 합해

            if cost_next < distance[node_next]: # 그 지점까지의 거리를 비교한다. 가장 작은 경우를 그 지점까지의 거리로 설정
                distance[node_next] = cost_next
                heapq.heappush(heap, [cost_next, node_next]) # 그 지점을 다음 이동 지점으로 설정하고 종료
    
    return distance
        
N, M, X = map(int, input().split())
graph = [[]*(N+1) for _ in range(N+1)]
# N 도시의 수, M 간선의 수, X 파티를 벌이는 도시 번호, maxtrix 인접행렬

for _ in range(M):
    S, E, T = map(int, input().split())
    graph[S].append([T, E]) # min heap은 기본적으로 첫번째 요소를 기준으로 정렬될것

answer = [0]*(N+1)
for i in range(1, N+1):
    arr = dijkstra(i, graph) # i에서 X까지 가는 거리 
    answer[i] += arr[X]
    arr2 = dijkstra(X, graph) # X에서 i로 오는 거리
    answer[i] += arr2[i]

print(max(answer))

