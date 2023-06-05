import sys
from collections import deque
input = sys.stdin.readline

def bfs():

    queue = deque()

    # 숫자 2로 표시된 좌표를 찾아서 큐에 추가
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 2:
                queue.append((i, j))
                dist[i][j] = 0  # 시작 지점의 거리를 0으로 설정

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            if graph[nx][ny] == 0:
                continue

            if dist[nx][ny] == -1:  # 방문하지 않은 칸일 경우에만 거리 갱신
                dist[nx][ny] = dist[x][y] + 1  # 이전 칸의 거리 + 1
                queue.append((nx, ny))

    return dist

n, m = map(int, input().split())

graph = []
for i in range(n):
    a = list(map(int, input().strip().split()))
    graph.append(a)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 각 칸까지의 최단 거리를 기록하는 2차원 리스트 생성 및 초기화
dist = [[-1 if graph[i][j] != 0 else 0 for j in range(m)] for i in range(n)]

bfs()

# 최단 거리 출력
for i in range(n):
    for j in range(m):
        print(dist[i][j], end=" ")
    print()
