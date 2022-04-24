hor = [chr(i) for i in range(ord('a'), ord('h')+1)]
ver = [i for i in range(1, 9)]
step = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]

start = list(input())
count = 0
for s in step:
    if chr(ord(start[0])+s[0]) in hor and int(start[1])+s[1] in ver:
        count += 1

print(count)
