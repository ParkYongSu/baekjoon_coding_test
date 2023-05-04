def solution(park, routes):
    h = len(park)
    w = len(park[0])

    point = [0, 0]

    for i in range(h):
        p = park[i]

        if "S" in p:
            point[0] = i
            point[1] = p.index("S")
            break

    for r in routes:
        route = r.split()
        direction = route[0]
        distance = int(route[1])
        pf = False

        if direction == "E":
            for i in range(distance):
                y = point[1] + (i + 1)
                if y >= w or park[point[0]][y] == "X":
                    pf = True
                    break

            if not pf:
                point[1] = point[1] + distance

        elif direction == "W":
            for i in range(distance):
                y = point[1] - (i + 1)
                if y < 0 or park[point[0]][y] == "X":
                    pf = True
                    break

            if not pf:
                point[1] = point[1] - distance

        elif direction == "N":
            for i in range(distance):
                y = point[0] - (i + 1)
                if y < 0 or park[y][point[1]] == "X":
                    pf = True
                    break

            if not pf:
                point[0] = point[0] - distance

        else:
            for i in range(distance):
                y = point[0] + (i + 1)
                print(y)
                if y >= h or park[y][point[1]] == "X":
                    pf = True
                    break

            if not pf:
                point[0] = point[0] + distance

    return point



print(solution(["0OO","OSO","OOO"],["E 2","S 2","W 1"]))