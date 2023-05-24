def solution(sequence, k):
    a = 0
    b = 0
    s = sequence[0]
    answer = []

    while True:
        if s < k:
            b += 1
            if b == len(sequence):
                break
            s += sequence[b]

        if s >= k:
            if s == k:
                answer.append([a, b])
            s -= sequence[a]
            a += 1

            if a == len(sequence):
                break

    answer.sort(key=lambda x: x[1] - x[0])
    return answer[0]


print(solution([1, 1, 1, 2, 3, 4, 5], 5))
