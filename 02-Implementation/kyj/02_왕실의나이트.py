n = list(input())
x, y = ord(n[0]), int(n[1])

nx, ny = x, y
cnt = 0

moves = [
[2,1],
[2,-1],

[-2,1],
[-2,-1],

[1,2],
[-1,2],

[1,-2],
[-1,-2],
]

for move in moves:

  nx = x + move[0]
  ny = y + move[1]
  
  if nx < ord('a') or ny < 1 or nx > ord('h') or ny > 8:
    continue 
  else:
    cnt+=1

print(cnt)
