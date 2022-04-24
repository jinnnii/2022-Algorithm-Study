
# n = int(input())
# arr = [list(input()) for _ in range(n)]

# max_count = 0


# def check(arr, srow, erow, scol, ecol):
#     result = 0
#     # 행 체크
#     for i in range(srow, erow+1):
#         cnt = 1
#         for j in range(1, n):
#             cnt = cnt+1 if arr[i][j-1] == arr[i][j] else 1
#             result = max(result, cnt)

#     # 열 체크
#     for i in range(scol, ecol+1):
#         cnt = 1
#         for j in range(1, n):
#             # result = max(result, [arr[_i][i]
#             #                       for _i in range(n)].count(arr[j-1][i]))
#             cnt = cnt+1 if arr[j-1][i] == arr[j][i] else 1
#             result = max(result, cnt)
#     return result


# for i in range(n):
#     for j in range(n):
#         if i < n-1:
#             arr[i][j], arr[i+1][j] = arr[i+1][j], arr[i][j]
#             max_count = max(max_count, check(arr, i, i+1, j, j))
#             arr[i][j], arr[i+1][j] = arr[i+1][j], arr[i][j]

#         if j < n-1:
#             arr[i][j], arr[i][j+1] = arr[i][j+1], arr[i][j]
#             max_count = max(max_count, check(arr, i, i, j, j+1))
#             arr[i][j], arr[i][j+1] = arr[i][j+1], arr[i][j]
# print(max_count)

n = int(input())
arr = [list(input()) for _ in range(n)]
max_count = 0


def check(arr, srow, erow, scol, ecol):
    return max(max_count,
               arr[srow].count(arr[srow][scol]),
               arr[erow].count(arr[erow][scol]),
               [arr[i][scol] for i in range(n)].count(arr[srow][scol]),
               [arr[i][ecol] for i in range(n)].count(arr[erow][ecol]))


for i in range(n):
    for j in range(n):
        if i < n-1:
            arr[i][j], arr[i+1][j] = arr[i+1][j], arr[i][j]
            max_count = check(arr, i, i+1, j, j)
            arr[i][j], arr[i+1][j] = arr[i+1][j], arr[i][j]

        if j < n-1:
            arr[i][j], arr[i][j+1] = arr[i][j+1], arr[i][j]
            max_count = check(arr, i, i, j, j+1)
            arr[i][j], arr[i][j+1] = arr[i][j+1], arr[i][j]
print(max_count)
