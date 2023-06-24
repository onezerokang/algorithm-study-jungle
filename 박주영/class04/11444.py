# 피보나치 수 6

# n이 주어졌을 때, n 번째 피보나치 수를 구하는 프로그램을 작성하시오.
# 메모리 초과

# import sys
# input = sys.stdin.readline

# n = int(input().rstrip())
# dp = [0] * (n+1)
# dp[1] = 1

# for i in range(2, n+1):
#     dp[i] = (dp[i-1] + dp[i-2]) % 1000000007
    
# print(dp[-1])


# 아주 큰 수의 피보나치: "행렬의 거듭제곱" 이랍니다.

import sys
input = sys.stdin.readline

n = int(input().rstrip())
matrix = [[1, 1], [1, 0]]

# 행렬의 곱셈
def mul_matrix(mat1, mat2):
    res = [[0] * 2 for _ in range(2)]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                res[i][j] += mat1[i][k] *mat2[k][j] % 1000000007
    return res

# 분할 정복
def power(a, b):
    if b == 1:
        return a
    else:
        tmp = power(a, b//2)
        if b%2 == 0:
            return mul_matrix(tmp, tmp)
        else:
            return mul_matrix(mul_matrix(tmp, tmp), a)

result = power(matrix, n)

print(result[0][1] % 1000000007)