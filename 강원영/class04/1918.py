import sys
input = sys.stdin.readline
a = input().rstrip()

operator = {"+": 0, "-": 0, "*": 1, "/": 1}
stack = []
ans = ""

for x in a:
    if x.isalpha():
        ans += x
    elif x == "(":
        stack.append(x)
    elif x == ")":
        while stack[-1] != "(":
            ans += stack.pop()
        stack.pop()
    else:
        while stack and stack[-1] != "(" and operator[stack[-1]] >= operator[x]:
            ans += stack.pop()
        stack.append(x)

while stack:
    ans += stack.pop()

print(ans)