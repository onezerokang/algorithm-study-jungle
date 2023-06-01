import sys
from collections import deque
input = sys.stdin.readline

def bfs(x, y):
    q = deque([(x, y)])
    graph[x][y] = 0

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M and graph[nx][ny]:
                graph[nx][ny] = 0
                q.append((nx, ny))

T = int(input())
for _ in range(T):           
    M, N, K = map(int, input().split())
    graph = [[0] * M for _ in range(N)]

    for _ in range(K):
        x, y = map(int, input().split())
        graph[y][x] = 1
    
    ans = 0
    for i in range(N):
        for j in range(M):
            if graph[i][j]:
                bfs(i, j)
                ans += 1
    print(ans)


