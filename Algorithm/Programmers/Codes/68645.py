"""

삼각 달팽이 : https://school.programmers.co.kr/learn/courses/30/lessons/68645

정수 n이 주어졌을 때, 밑변의 길이와 높이가 n인 삼각형에서 달팽이 채우기를 진행한 후, 첫 행부터 마지막 행까지 모두 순서대로 합친 결과를 구하는 문제
- 달팽이 채우기 방법은 다음과 같다
    - 맨 위 꼭짓점부터 시작하여 반시계 방향으로 진행하며 1씩 증가하는 값을 채워 넣는다
- n은 1 이상 1,000 이하의 정수이다

Example:
- Input : n=4
- Output : [1,2,9,3,10,8,4,5,6,7]

- Input : n=5
- Output : [1,2,12,3,13,11,4,14,15,10,5,6,7,8,9]

- Input : n=6
- Output : [1,2,15,3,16,14,4,17,21,13,5,18,19,20,12,6,7,8,9,10,11]

Note:
삼각형 형태의 이차원 배열 arr 생성
하단으로 내려가는 방향 (i % 3 == 0) / 우측으로 이동하는 방향 (i % 3 == 1) / 좌상단으로 올라가는 방향 (i % 3 == 2)
세 가지로 구분하여 위치를 변경하며 배열을 채우는 방법

"""

def solution(n):
    arr = [[0] * i for i in range(1, n+1)]

    x, y = -1, 0
    num = 1

    for i in range(n):
        for j in range(i, n):
            if i % 3 == 0:
                x += 1
            elif i % 3 == 1:
                y += 1
            else:
                x -= 1
                y -= 1
            arr[x][y] = num
            num += 1

    return [y for x in arr for y in x]