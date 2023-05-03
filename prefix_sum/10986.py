import sys

input = sys.stdin.readline

n, m = map(int, input().split())
o = list(map(int, input().split()))
c = [0] * m
count = 0
total = 0

for i in range(n):
    total += o[i]
    remain = total % m
    if remain == 0: count += 1
    c[remain] += 1

for i in range(m):
    if c[i] > 1 :
        count += c[i] * (c[i] - 1) // 2

print(count)

