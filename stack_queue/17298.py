import sys

n = int(input())
l = list(map(int, input().split()))
ans = [0] * n
stack = []

for i in range(n):
    target = l[i]
    while stack and l[stack[-1]] < target:
        ans[stack.pop()] = target
    stack.append(i)

while stack:
    ans[stack.pop()] = -1

for i in range(n):
    sys.stdout.write(str(ans[i]) + " ")


