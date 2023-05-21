# 상근이는 설탕을 배달하려 할 때, 3kg과 5kg 봉지가 있다.

# 상근이가 설탕을 정확하게 N킬로그램 배달해야 할 때,
# 봉지 갯수를 최소로 하려 할 때 몇 개를 가져가면 되는지
# 그 수를 구하는 프로그램을 작성하시오.

import sys
input = sys.stdin.readline

N = int(input().rstrip())

def findNum(weight):
    idx = weight // 5
    rest = 0
    for i in range(idx, -1, -1):
        rest = weight - (i*5)
        if rest % 3 == 0:
            return (i + int(rest//3))
        if i == 0 and rest // 3 == 0:
            return int(rest//3)
    return -1

print(findNum(N))