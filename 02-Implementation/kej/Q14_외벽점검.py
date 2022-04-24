# n : 외벽의 총 둘레 미터
# weak : 취약 지점 위치
# dist : 각 친구가 1시간동안 이동할 수 있는 거리

import itertools


def solution(n, weak, dist):
    wn = len(weak)
    # weak 원형을 일렬로
    for i in range(wn):
        weak.append(weak[i]+n)

    answer = len(dist)+1

    for start in range(wn):
        for friends in list(itertools.permutations(dist, len(dist))):
            count = 1  # 투입할 친구 수

            # 현재 친구가 점검 가능한 위치 구하기
            position = weak[start]+friends[count-1]
            # 시작점 부터 모든 취약지점 확인
            for i in range(start, start+wn):
                if position < weak[i]:
                    count += 1
                    if count > len(dist):
                        break
                    position = weak[i]+friends[count-1]

            answer = min(count, answer)

    if answer > len(dist):
        return -1
    return answer


d = solution(12, [1, 5, 6, 10], [3, 5, 7])
print(d)
