import sys
from collections import deque

input = sys.stdin.readline

n, l = map(int, input().split())
o = list(map(int, input().split()))
d = deque()

for i in range(n):
    while d and d[-1][1] > o[i]:
        d.pop()
    while d and d[0][0] < i - l + 1:
        d.popleft()
    d.append((i, o[i]))
    print(d[0][1], end = ' ')


