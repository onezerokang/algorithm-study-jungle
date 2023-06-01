import sys
input = sys.stdin.readline

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        fib = [0] * (n + 1)
        fib[0] = 0
        fib[1] = 1
        for i in range(2, n + 1):
            fib[i] = fib[i - 1] + fib[i - 2]
        return fib[n]

def count_zeros_ones(n):
    if n == 0:
        return (1, 0)
    elif n == 1:
        return (0, 1)
    else:
        fib_zero = [0] * (n + 1)
        fib_one = [0] * (n + 1)
        fib_zero[0] = 1
        fib_one[1] = 1
        for i in range(2, n + 1):
            fib_zero[i] = fib_zero[i - 1] + fib_zero[i - 2]
            fib_one[i] = fib_one[i - 1] + fib_one[i - 2]
        return (fib_zero[n], fib_one[n])

t = int(input())  # 테스트 케이스 개수 입력
for _ in range(t):
    n = int(input())  # n 값 입력
    result = count_zeros_ones(n)
    print(result[0], result[1])
