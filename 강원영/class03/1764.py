import sys
input = sys.stdin.readline

N, M = map(int, input().split())

set1 = set([input().rstrip() for _ in range(N)])
set2 = set([input().rstrip() for _ in range(M)])

ans = sorted(list(set1.intersection(set2)))
print(len(ans))
for name in ans:
    print(name)
