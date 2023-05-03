def sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    less = []
    equal = []
    greater = []

    for e in arr:
        if e[0] < pivot[0]:
            less.append(e)
        elif e[0] > pivot[0]:
            greater.append(e)
        else:
            if e[1] < pivot[1]:
                less.append(e)
            elif e[1] > pivot[1]:
                greater.append(e)
            else:
                equal.append(e)

    return sort(less) + equal + sort(greater)


n = int(input())
a = [[0, 0] for _ in range(n)]

for i in range(n):
    a[i] = list(map(int, input().split()))

a = sort(a)

for e in a:
    print(str(e[0]) + " " + str(e[1]))