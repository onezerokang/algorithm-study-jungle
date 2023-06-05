# logic
# 상하좌우 방문여부 따지네..bfs 문제
# 준비물 : 지도, 지도내의 목표지점 표시, 지도내의 벽 표시,이동 좌표들의 deque + 거리 표시할 리스트
# 입력값 받으면서 목표지점 방문 표시하고 벽 표시해서
# bfs 돌면서 벽 아니면서 방문안했으면서 갈 수 있는 땅의 누적합을  거리 표시할 리스트에 넣기
from sys import stdin
from collections import deque
n, m = map(int, stdin.readline().strip().split())
map_ = [[] for _ in range(n)] #좌표
visited = [[False]*m for _ in range(n)] #방문여부
q = deque([]) 
ans = [[-1]*m for _ in range(n)] #현좌표까지의 거리 
for i in range(n):
    r = list(map(int, stdin.readline().strip().split()))
    for j in range(m):
        if r[j] == 2: # 목표지점 표시
            q.append((i, j))
            visited[i][j] = True
            ans[i][j] = 0
        if r[j] == 0: # 벽 표시
            ans[i][j] = 0
    map_[i]=r
d = [[-1, 0], [1, 0], [0, -1], [0, 1]]
while q: #bfs
    x, y = q.popleft()
    for dir_ in d:
        nx, ny = x+dir_[0], y+dir_[1]
        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and map_[nx][ny] == 1:
            q.append((nx, ny))
            visited[nx][ny] = True
            ans[nx][ny] = ans[x][y] + 1
for i in ans:
    for j in i:
        print(j, end=" ")
    print()
