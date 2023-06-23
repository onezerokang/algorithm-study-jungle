# 웜홀

# N개의 지점, N개의 지점 사이에는 M개의 도로와 W개의 웜홀이 있다.
# 도로는 방향이 없으나 웜홀은 방향이 있고, 시간이 반대로 흐른다.

# 출발하였을 때보다 시간이 과거로 돌아가는 경우가 있는지 확인하고 싶다.

# 음수 가중치를 가지는 edge가 있으니 벨만-포드

import sys
input = sys.stdin.readline
INF = 1e9

def bf(Edges, Dist, N):
    for i in range(N):
        for j in range(len(Edges)):
            now, next, cost = edges[j]
            if Dist[next] > Dist[now] + cost:
                Dist[next] = Dist[now] + cost
                if i == N - 1:
                    return True
    return False

TC = int(input().rstrip())
for _ in range(TC):
    N, M, W = map(int, input().split())
    # N: 지점의 수, M: 도로의 개수, W: 웜홀의 갯수
    edges = []
    dist = [INF] * (N+1)

    for _ in range(M): # 도로의 수, 도로는 양방향
        S, E, T = map(int, input().split())
        edges.append([S, E, T])
        edges.append([E, S, T])

    for _ in range(W): # 웜홀의 수
        S, E, T = map(int, input().split())
        T = -T # 줄어드는 시간, 양수로 주어지므로 음수로 바꾸어주자.
        edges.append([S, E, T])

    ans = bf(edges, dist, N)

    if ans == True:
        print("YES")
    else:
        print("NO")
