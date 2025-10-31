"""

행렬과 연산 : https://school.programmers.co.kr/learn/courses/30/lessons/118670

행렬과 적용할 연산들이 주어졌을 때, 연산을 차례대로 시행한 후의 행렬 상태를 구하는 문제
- ShiftRow 연산은 다음과 같다
    - 모든 행이 아래쪽으로 한 칸씩 밀려난다. 즉, 모든 행에 대해서 i번째 행은 i+1번째 행이 된다
    - 마지막 행은 1번째 행이 된다
- Rotate 연산은 다음과 같다
    - 행렬의 바깥쪽에 있는 원소들을 시계 방향으로 한 칸씩 회전시킨다
    - 행렬의 바깥쪽에 있는 원소들은 첫 행, 첫 열, 끝 행, 끝 열에 포함되는 원소들이다
- rc의 행 길이와 열 길이는 2 이상 50,000 이하이며, 행 길이와 열 길이의 곱은 4 이상 100,000 이하이다
- rc의 원소는 1 이상 1,000,000 이하의 정수이다
- operations의 길이는 1 이상 100,000 이하이다
    - operations의 원소는 "ShiftRow" 혹은 "Rotate"이다

Example:
- Input : rc=[[1, 2, 3], [4, 5, 6], [7, 8, 9]], operations=["Rotate", "ShiftRow"]
- Output : [[8, 9, 6], [4, 1, 2], [7, 5, 3]]

- Input : rc=[[8, 6, 3], [3, 3, 7], [8, 4, 9]], operations=["Rotate", "ShiftRow", "ShiftRow"]
- Output : [[8, 3, 3], [4, 9, 7], [3, 8, 6]]

- Input : rc=[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]], operations=["ShiftRow", "Rotate", "ShiftRow", "Rotate"]
- Output : [[1, 6, 7 ,8], [5, 9, 10, 4], [2, 3, 12, 11]]

Note:
단순하게 list에서 그대로 구현하면 효율성 테스트에서 시간 초과 발생
원소의 삽입 및 삭제를 효율적으로 할 수 있는 deque 이용
가장 왼쪽 열과 오른쪽 열은 별도로 left_col, right_col로 구분하고, 안에 있는 행들은 rows로 관리
테두리 원소들을 따로 관리함으로써 rotate 연산을 효율적으로 수행 가능

"""

from collections import deque

def solution(rc, operations):
    def shiftRow():
        rows.appendleft(rows.pop())
        left_col.appendleft(left_col.pop())
        right_col.appendleft(right_col.pop())

    def rotate():
        rows[-1].append(right_col.pop())
        left_col.append(rows[-1].popleft())
        rows[0].appendleft(left_col.popleft())
        right_col.appendleft(rows[0].pop())

    height = len(rc)
    rows = deque(deque(row[1:-1]) for row in rc)
    left_col = deque(rc[i][0] for i in range(height))
    right_col = deque(rc[i][-1] for i in range(height))

    for op in operations:
        if op == "Rotate":
            rotate()
        elif op == "ShiftRow":
            shiftRow()

    result = []
    for i in range(height):
        temp = [left_col[i]] + list(rows[i]) + [right_col[i]]
        result.append(temp)

    return result