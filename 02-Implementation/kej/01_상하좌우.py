n = int(input())
plans = input().split()
ls = {'L': (0, -1), 'R': (0, 1), 'U': (-1, 0), 'D': (1, 0)}
start = [1, 1]

for p in plans:
    if start[0]+ls[p][0] > 0 and start[1]+ls[p][1] > 0:
        start[0] += ls[p][0]
        start[1] += ls[p][1]

print(start)
