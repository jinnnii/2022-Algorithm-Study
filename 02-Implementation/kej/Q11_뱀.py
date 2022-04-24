def turn(d, c):
    if c == 'L':
        return (d-1) % 4
    else:
        return (d+1) % 4


n = int(input())
apple = int(input())
maps = [[0]*n for _ in range(n)]
direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]
info = []
count = 0

for _ in range(apple):
    y, x = map(int, input().split())
    maps[y-1][x-1] = 1

dn = int(input())

for _ in range(dn):
    c, d = input().split()
    info.append((int(c), d))


maps[0][0] = 2
snake = [[0, 0]]
x, y, d = [0, 0, 0]

while True:
    sx = x+direction[d][0]
    sy = y+direction[d][1]

    if sx in range(n) and sy in range(n):
        if maps[sy][sx] == 2:
            break

        if maps[sy][sx] == 1:
            snake.append([sx, sy])
            maps[sy][sx] = 2

        else:
            maps[sy][sx] = 2
            snake.append([sx, sy])
            px, py = snake.pop(0)
            maps[py][px] = 0
    else:
        break
    count += 1
    x = sx
    y = sy

    if info and info[0][0] == count:
        d = turn(d, info[0][1])
        info.pop(0)

print(count+1)
