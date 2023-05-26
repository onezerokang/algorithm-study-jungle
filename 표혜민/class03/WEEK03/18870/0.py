# 1 ≤ N ≤ 1,000,000
# -109 ≤ Xi ≤ 109
# 좌표 압출
# Xi >Xj 를 만족하는 서로 다른 좌표의 개수

from sys import stdin
N = int(stdin.readline().strip())
X = list(map(int, stdin.readline().strip().split()))
cpy  = list(set([*X]))
cpy.sort()
ans,cnt={},0
for i in cpy:
    ans[i] = cnt
    cnt+=1
for idx in X:
    print(ans[idx],end=" ")
