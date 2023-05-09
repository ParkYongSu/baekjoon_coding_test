def solution(n, m, section):
    count = 0

    while section:
        e = section[0] + m
        while section and section[0] < e:
            section.pop(0)

        count += 1

    return count