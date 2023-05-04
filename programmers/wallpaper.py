def solution(wallpaper):
    sharp = []
    x = len(wallpaper)
    y = len(wallpaper[0])

    for i in range(x):
        for j in range(y):
            e = wallpaper[i][j]
            if e == "#":
                sharp.append([i, j])

    first_x = sharp[0]
    end_x = sharp[len(sharp) - 1]

    sharp = sort_by_y(sharp)

    first_y = sharp[0]
    end_y = sharp[len(sharp) - 1]

    return [first_x[0], first_y[1], end_x[0] + 1, end_y[1] + 1]



def sort_by_y(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    less = sort_by_y(arr[:mid])
    higher = sort_by_y(arr[mid:])

    return sort(less, higher)


def sort(less, higher):
    l = 0
    h = 0
    merge = []

    while l < len(less) and h < len(higher):
        if less[l][1] > higher[h][1]:
            merge.append(higher[h])
            h += 1
        else:
            merge.append(less[l])
            l += 1

    while l < len(less):
        merge.append(less[l])
        l += 1

    while h < len(higher):
        merge.append(higher[h])
        h += 1

    return merge


print(solution([".##...##.", "#..#.#..#", "#...#...#", ".#.....#.", "..#...#..", "...#.#...", "....#...."]))
