import sys
from itertools import combinations
n, dn = map(int, input().split())
map = [list(map(int, input().split())) for _ in range(n)]

houses = []
chickens = []
result = sys.maxsize


def check_dir(chc):
    sum = 0
    for hx, hy in houses:
        dir = 2*n
        for cx, cy in chc:
            dir = min(abs(hx-cx) + abs(hy-cy), dir)
        sum += dir
    return sum


for x in range(n):
    for y in range(n):
        if map[x][y] == 1:
            houses.append([x, y])
        elif map[x][y] == 2:
            chickens.append([x, y])

for chc in combinations(chickens, dn):
    result = min(check_dir(chc), result)

print(result)
