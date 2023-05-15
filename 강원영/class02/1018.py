N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]
result = []

for i in range(N - 7):
    for j in range(M - 7):
        black_start = 0 # 시작 좌표가 검정색일 때 짝수가 검정색이어야 한다.
        white_start = 0 # 시작 좌표가 흰색일 때 짝수가 흰색이어야 한다.

        for a in range(i, i + 8):
            for b in range(j, j + 8):
                if (a + b) % 2 == 0:
                    if board[a][b] != "B":
                        black_start += 1
                    else:
                        white_start += 1
                else:
                    if board[a][b] != "W":
                        black_start += 1
                    else:
                        white_start += 1
        
        result.append(black_start)
        result.append(white_start)

print(min(result))