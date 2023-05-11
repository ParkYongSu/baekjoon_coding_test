def common_divisor(a, b):
    less = min(a, b)
    higher = max(a, b)

    n = higher % less
    while n != 0:
        higher = less
        less = n
        n = higher % less
    return less


n = int(input())
answer = []

for i in range(n):
    a, b = map(int, input().split())

    c = common_divisor(a, b)
    answer.append(c * (a // c) * (b // c))

for e in answer:
    print(e)