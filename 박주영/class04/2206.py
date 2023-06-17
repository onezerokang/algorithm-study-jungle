# 벽 부수고 이동하기
# (0, 0) -> (N, M) 최단거리, 한 번 벽을 부술 기회가 있음

import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())

matrix = [([0] * M) for _ in range(N)]

for i in range(N):
    matrix[i] = list(map(int, input().strip()))

def bfs(arr):
    # visited = [([0] * M) for _ in range(N)]
    visited = [[[0] * 2 for _ in range(M)] for _ in range(N)] # 3 차원, 두 페이즈로 나누어 bfs 진행하면 된다.
    visited[0][0][0] = 1
    
    q = deque()
    q.append([0, 0, 0])
    
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    while q:
        x, y, c = q.popleft()
        
        if x == M-1 and y == N-1:
            print(visited[y][x][c])
            return

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if (0 <= nx < M and 0 <= ny < N):
                nPoint = arr[ny][nx]

                if (nPoint == 0 and not visited[ny][nx][c]):
                    q.append([nx, ny, c])
                    visited[ny][nx][c] = visited[y][x][c] + 1

                elif (nPoint == 1 and c == 0):
                    q.append([nx, ny, 1])
                    visited[ny][nx][1] = visited[y][x][0] + 1
                    
                    # mx = nx + dx[i]
                    # my = ny + dy[i]
                    # if ((0 <= mx < M and 0 <= ny < N) and
                    #     not visited[my][mx] and arr[my][mx] == 0):
                    #     q.append([mx, my])
                    #     visited[ny][nx] = visited[y][x] + 1
                    #     visited[my][mx] = visited[ny][nx]+ 1
                    #     cnt = 0
    print(-1)
    return

bfs(matrix)