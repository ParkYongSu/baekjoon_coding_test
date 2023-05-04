def solution(players, callings):
    answer = {i: p for i, p in enumerate(players)}
    keys = {p: i for i, p in enumerate(players)}

    for call in callings:
        player_idx = keys[call]
        front_player = answer[player_idx - 1]

        answer[player_idx] = answer[player_idx - 1]
        keys[front_player] = player_idx
        answer[player_idx - 1] = call
        keys[call] = player_idx - 1

    return list(answer.values())


print(solution(["mumu", "soe", "poe", "kai", "mine"], ["kai", "kai", "mine", "mine"]))

