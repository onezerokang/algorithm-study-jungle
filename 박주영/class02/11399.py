# ATM
# N명의 사람이 하나의 ATM에 서 있고, 이 사람들이 인출하는데 걸리는 시간은 각각 다르다
# 임의의 순서로 돈을 인출할 때, 모든 사람이 돈을 인출하는 데 걸리는 시간의 합이 최소가 되는 
# 인출 순서는?

import sys
input = sys.stdin.readline

N = int(input().rstrip())
times = list(map(int, (input().split())))

# 모든 사람이 인출하는 시간의 합이 최소가 되려면 겹치는 시간(뒤에 대기하는 사람들)이
# 작은 시간들이 되어야 한다.
# 즉 제일 먼저 처리해야 하는 사람들은 시간이 가장 오래걸리는 사람들임

def atm(arr):
    ans = 0
    arr.sort()
    for i in range(len(arr)):
        for j in range(i+1):
            ans += arr[j]
    print(ans)

atm(times)