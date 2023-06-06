import sys
from collections import deque
input = sys.stdin.readline

def get_starting_coord():
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 2:
                return (i, j)

def bfs(x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    dq = deque([(x, y)])
    graph[x][y] = 0
    visited[x][y] = True

    while dq:
        x, y = dq.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and graph[nx][ny] == 1:
                dq.append((nx, ny))
                graph[nx][ny] = graph[x][y] + 1
                visited[nx][ny] = True

def print_result():
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1 and not visited[i][j]:
                graph[i][j] = -1
            print(graph[i][j], end=" ")
        print("")

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

x, y = get_starting_coord()
bfs(x, y)
print_result()