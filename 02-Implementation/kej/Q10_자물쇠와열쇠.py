# key : [[0, 0, 0], [1, 0, 0], [0, 1, 1]] >>>> lock: [[1, 1, 1], [1, 1, 0], [1, 0, 1]] >>>>> true

def rotate(key):
    n = len(key)
    m = len(key[0])
    result = [[0]*n for _ in range(m)]
    # print(result)
    for i in range(n):
        for j in range(m):
            result[j][n-1-i] = key[i][j]
    return result


def check(arr):
    n = len(arr)//3
    for i in range(n, n*2):
        for j in range(n, n*2):
            if arr[i][j] != 1:
                return False
    return True


def solution(key, lock):
    n = len(key)
    m = len(lock)
    new_lock = [[0]*(m*3) for _ in range(m*3)]
    for i in range(m):
        for j in range(m):
            new_lock[i+m][j+m] = lock[i][j]

    for rotation in range(4):
        key = rotate(key)
        for x in range(m*2):
            for y in range(m*2):
                for i in range(n):
                    for j in range(n):
                        new_lock[x+i][y+j] += key[i][j]
                if check(new_lock) == True:
                    return True
                for i in range(n):
                    for j in range(n):
                        new_lock[x+i][y+j] -= key[i][j]
    return False


result = solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]],
                  [[1, 1, 1], [1, 1, 0], [1, 0, 1]])
print(result)
