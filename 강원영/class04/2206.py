# 벽 부수고 이동하기
import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [list(map(int, list(input().rstrip()))) for _ in range(N)]
visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]

def bfs(n, m):
    dq = deque()
    dq.append([0, 0, 0])
    visited[0][0][0] = 1
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while dq:
        x, y, z = dq.popleft()

        if x == n - 1 and y == m - 1:
            return visited[x][y][z]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            # 이동할 부분인 벽인데, 벽을 부순적이 없다.
            if graph[nx][ny] == 1 and z == 0:
                visited[nx][ny][1] = visited[x][y][0] + 1
                dq.append([nx, ny, 1])           
            # 앞이 벽이 아니고 방문한적이 없다.
            elif graph[nx][ny] == 0 and visited[nx][ny][z] == 0:
                visited[nx][ny][z] = visited[x][y][z] + 1
                dq.append([nx, ny, z]) 
    
    return - 1

print(bfs(N, M))