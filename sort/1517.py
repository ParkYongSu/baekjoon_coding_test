result = 0


def merge(less, high):
    global result
    l = 0
    h = 0
    merged = []

    while l < len(less) and h < len(high):
        e_l = less[l]
        e_h = high[h]
        if e_l > e_h:
            merged.append(e_h)
            result = result + (len(less) - l)
            h += 1
        else:
            merged.append(e_l)
            l += 1
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
l = list(map(int, input().split()))
merge_sort(l)
print(result)
