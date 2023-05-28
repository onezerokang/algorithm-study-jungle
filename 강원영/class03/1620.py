import sys
input = sys.stdin.readline

N, M = map(int, input().split())
pokemons1 = [""] + [input().rstrip() for _ in range(1, N + 1)] # index 접근용
pokemons2 = { value : index for index, value in enumerate(pokemons1) } # key 접근용

for _ in range(M):
    quiz = input().rstrip()
    if quiz.isdecimal():
        print(pokemons1[int(quiz)])
    else:
        print(pokemons2[quiz])