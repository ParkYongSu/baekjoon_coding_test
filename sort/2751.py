import sys


def merge(less, high):
    l = 0
    h = 0
    merged = []

    while l < len(less) and h < len(high):
        e_l = less[l]
        e_h = high[h]
        if e_l < e_h:
            merged.append(e_l)
            l += 1
        else:
            merged.append(e_h)
            h += 1
    while l < len(less):
        merged.append(less[l])
        l += 1

    while h < len(high):
        merged.append(high[h])
        h += 1

    return merged


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    m = len(arr) // 2
    less = merge_sort(arr[:m])
    high = merge_sort(arr[m:])

    return merge(less, high)


n = int(input())
a = []

for i in range(n):
    a.append(int(sys.stdin.readline()))

a = merge_sort(a)

for e in a:
    print(e)