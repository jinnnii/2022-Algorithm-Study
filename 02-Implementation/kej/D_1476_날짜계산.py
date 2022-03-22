year = list(map(int, input().split()))
c_year = [0, 0, 0]
result = 0

while c_year != year:
    c_year[0] = 1 if c_year[0] >= 15 else c_year[0]+1
    c_year[1] = 1 if c_year[1] >= 28 else c_year[1]+1
    c_year[2] = 1 if c_year[2] >= 19 else c_year[2]+1
    result += 1
print(result)
