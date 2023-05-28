import sys

def get_coords():
    input = sys.stdin.readline
    N = int(input())
    coords = list(map(int, input().split()))
    return coords

def compress_coords(coords):
    coords2 = {}
    for i, c in enumerate(sorted(set(coords))):
        coords2[c] = i
    return [coords2[c] for c in coords]

coords = get_coords()
answer = compress_coords(coords)

for a in answer:
    print(a, end=" ")