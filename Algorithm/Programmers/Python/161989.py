"""

덧칠하기 : https://school.programmers.co.kr/learn/courses/30/lessons/161989

길이가 n미터인 벽에 페인트를 새로 칠해야 하는 구역과 페인트를 칠하는 롤러의 길이가 주어졌을 때, 롤러로 페인트를 칠해야 하는 최소 횟수를 구하는 문제
- 벽은 1미터 길이의 구역 n개로 나누고, 각 구역에 왼쪽부터 순서대로 1번부터 n번까지 번호가 부여되어 있다
- 길이 m인 롤러로 벽에 페인트를 한 번 칠하는 규칙은 다음과 같다
    - 롤러가 벽에서 벗어나면 안 된다
    - 구역의 일부분만 포함되도록 칠하면 안 된다
    - 롤러의 좌우측 끝을 구역의 경계선 혹은 벽의 좌우측 끝부분에 맞추어 완전히 칠하는 것을 한 번 칠했다고 정의한다
- 벽의 길이 n과 롤러의 길이 m은 1 이상 100,000 이하의 정수이며, m <= n을 만족한다
- 페인트를 칠해야 하는 구역의 번호가 담긴 정수 배열 section의 길이는 1 이상 n 이하이다
    - section의 원소는 1 이상 n 이하이다
    - section에서 같은 원소가 두 번 이상 나타나지 않는다
    - section의 원소는 오름차순으로 정렬되어 있다

Example:
- Input : n=8, m=4, section=[2, 3, 6]
- Output : 2

- Input : n=5, m=4, section=[1, 3]
- Output : 1

- Input : n=4, m=1, section=[1, 2, 3, 4]
- Output : 4

Note:
리스트에서 효율적으로 제거하기 위해 deque 사용
한 구역을 칠하면 롤러가 닿는 영역까지는 무조건 칠하게 되므로, 범위 내에 있는 section의 원소는 제거

"""

from collections import deque

def solution(n, m, section):
    answer = 0
    wall = deque([s for s in section])

    while wall:
        start = wall.popleft()
        answer += 1
        while wall:
            if wall[0] <= start + m - 1:
                wall.popleft()
            else:
                break

    return answer