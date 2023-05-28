# 1 ≤ N ≤ 1,000,000
# -109 ≤ Xi ≤ 109
# 좌표 압출
# Xi >Xj 를 만족하는 서로 다른 좌표의 개수
# logic
# 입력값 배열 X를 set에 넣어 중복을 없앤 배열을 만들기
# 중복 없는 배열의 값을 key로하고 값으로 순위를 매겨준 dict을 만들어주기
# X의 값들을 dict의 key값으로 접근하여 value를 한줄로 출력해주기
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
