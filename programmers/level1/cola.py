def solution(a, b, n):
    answer = 0
    while True:
        r = n % a
        m = (n // a) * b
        n = m + r
        answer += m
        if n < a:
            break

    return answer


print(solution(2, 1, 100))