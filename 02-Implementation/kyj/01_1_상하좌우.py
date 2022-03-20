num = input()
move = input().split()
position_X = 1
position_Y = 1
print(num,move)

for i in move:
  if i == 'R':
    position_X += 1
  elif i ==  'U':
    if position_Y > 1:
      position_Y -= 1
  elif i == 'L':
    position_X -= 1
  elif i ==  'D':
      position_Y += 1

  print(">>",position_X,position_Y)

print(position_X,position_Y)


#### 답안

n = input()
x, y = 1, 1
plans = input().split()

#L, R, U, D 에  따른 이동 방향
dx = [0,0,-1,1]
dy = [-1,1,0,0]
move_types = ['L','R','U','D']

#이동 계획을 하나씩 확인
for plan in plans:
	#이동 후 좌표 구하기
	for i in range(len(move_types)):
		if plan == move_types[i]:
			nx = x + dx[i]
			ny = y + dy[i]
	#공간을 벗어나는 경우 이동 무시
	if nx < 1 or ny<1 or nx > n or ny > n:
		continue

	#이동 수행
	x, y = nx, ny