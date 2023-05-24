import math


def solution(r1, r2):
    answer = 0
    for i in range(1, r2+1) :
        if r1**2 - i**2 >= 0 :
            low = math.ceil(math.sqrt(r1**2 - i**2))
        else :
            low = 0
        high = math.floor(math.sqrt(r2**2 - i**2))
        answer += (high - low + 1)
    return answer * 4



print(solution(2, 3))
