def solution(s, skip, index):
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
                "v", "w", "x", "y", "z"]
    answer = ""

    for i in skip:
        alphabet.remove(i)
    for j in s:
        answer += alphabet[(alphabet.index(j) + index) % len(alphabet)]
    return answer


print(solution("aukks", "wbqd", 5))
