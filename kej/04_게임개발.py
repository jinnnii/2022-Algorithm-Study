n, m = map(int, input().split())
x, y, d = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]
# n, m = (4, 4)
# x, y, d = (1, 1, 0)
# maps = [[1, 1, 1, 1], [1, 0, 0, 1], [1, 1, 0, 1], [1, 1, 1, 1]]

news = {0: (-1, 0), 1: (0, 1), 2: (1, 0), 3: (0, -1)}
count = 1

print(maps)


def turn(d):
    d -= 1
    if d == -1:
        d = 3
    return d


while maps[x][y] != 1:
    for _ in range(4):
        d = turn(d)
        _x = news[d][0]
        _y = news[d][1]
        if x+_x not in range(n) or y+_y not in range(m):
            continue
        next_pos = maps[x+_x][y+_y]
        if next_pos == 0:
            maps[x][y] = 2
            x += _x
            y += _y
            count += 1
            print(maps[0], x, y, d)
            print(maps[1])
            print(maps[2])
            print(maps[3])
            print()
            break
    else:
        maps[x][y] = 2
        x -= news[d][0]
        y -= news[d][1]

print(count)
