def check(build):
    for x, y, f in build:
        # 기둥인 경우
        if f == 0:
            if y == 0 or [x, y-1, 0] in build or [x-1, y, 1] in build or [x, y, 1] in build:
                continue
            return False
        # 보인 경우
        else:
            if [x-1, y, 1] in build and [x+1, y, 1] in build or [x+1, y-1, 0] in build or [x, y-1, 0] in build:
                continue
            return False
    return True


def solution(build_frame):
    build = []
    for x, y, f, b in build_frame:
        # x,y : 설치 또는 삭제할 기둥 및 보의 좌표
        # f : 설치 또는 삭제할 기둥(0) 및 보(1)
        # b : 삭제(0) 및 설치(1)

        # 삭제할 경우
        if b == 0:
            build.remove([x, y, f])
            if not check(build):
                build.append([x, y, f])
        else:
            build.append([x, y, f])
            if not check(build):
                build.remove([x, y, f])

    return sorted(build)


result = solution([[1, 0, 0, 1], [1, 1, 1, 1], [2, 1, 0, 1], [2, 2, 1, 1],
                   [5, 0, 0, 1], [5, 1, 0, 1], [4, 2, 1, 1], [3, 2, 1, 1]])
print(result)
