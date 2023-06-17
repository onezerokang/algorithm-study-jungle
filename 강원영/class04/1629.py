import sys
input = sys.stdin.readline

A, B, C = map(int, input().split())

def pow(a, b):
    if b == 1:
        return a % C
    
    x = pow(a, b // 2)
    if b % 2 == 0:
        return x * x % C
    else:
        return x * x * a % C
    
print(pow(A, B))