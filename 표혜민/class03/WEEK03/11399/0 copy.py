# logic
from sys import stdin
N = int(stdin.readline().strip())
p = {idx+1: i for idx, i in enumerate(
    list(map(int, stdin.readline().strip().split())))}
# print(p)
ans = []
# for i in p:
i = 1
while p:
    try:
        if p[i] == min(*p.values()): #최소인 값들 뺴주기
            ans.append(i)
            p.pop(i)
    except:
        
        print(p.keys())
        for item in p.keys():
            if p[item] ==min(*p.values()):
                ans.append(item)
                p.pop(item)
        break
    i += 1
print(ans)
