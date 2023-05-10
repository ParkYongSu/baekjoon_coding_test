def solution(number, limit, power):
    c = []
    for n in range(1, number + 1):
        count = 0
        for i in range(1, int(n ** (1 / 2)) + 1):
            if n % i == 0:
                count += 1
                if i ** 2 != n:
                    count += 1
        c.append(count)
    res = [i if i <= limit else power for i in c]

    return res


print(solution(10, 3, 2))
