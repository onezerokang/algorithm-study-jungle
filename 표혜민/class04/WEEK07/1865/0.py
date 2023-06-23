from sys import stdin
TC = int(stdin.readline().strip())

for i in range(TC):
    graph = []
    N, M, W = map(int, stdin.readline().strip().split())
    # print(N, M, W,"!!")
    for _ in range(M+1):
        S, E, T = map(int, stdin.readline().strip().split())
        print(S, E, T)
    print()
    # print("YES") if 시간이 줄어들면서 출발위치로 돌아옴 else print("NO")

# 벨멘 포드 공부를 하고 다시 풀자!