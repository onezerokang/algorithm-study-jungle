import sys
input = sys.stdin.readline

# N, M = map(int, input().split())

# pokemon = []
# for _ in range(N):
#     name = input().rstrip()
#     pokemon.append(name)

# for _ in range(M):
#     choice = input().rstrip()
#     if choice.isdigit():
#         number = int(choice)
#         print(pokemon[number - 1])
#     elif choice.isalpha():
#         for z, item in enumerate(pokemon):
#             if item == choice:
#                 print(z+1)

# 시간 초과

# N, M = map(int, input().split())

# pokemon = {}
# for i in range(N):
#     name = input().rstrip()
#     pokemon[name] = str(i + 1)

# for _ in range(M):
#     choice = input().rstrip()
#     if choice.isdigit():
#         number = int(choice)
#         print(list(pokemon.keys())[number-1])
#     elif choice.isalpha():
#         print(pokemon.get(choice))

# 시간 초과

N, M = map(int, input().split())

pokemon = {}
pokemon_reverse = {}
for i in range(N):
    name = input().rstrip()
    pokemon[name] = i + 1
    pokemon_reverse[i + 1] = name

for _ in range(M):
    choice = input().rstrip()
    if choice.isdigit():
        number = int(choice)
        print(pokemon_reverse.get(number))
    elif choice.isalpha():
        print(pokemon.get(choice))