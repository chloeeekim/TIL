"""

키패드 누르기 : https://school.programmers.co.kr/learn/courses/30/lessons/67256

입력해야 하는 숫자와 오른손잡이인지 왼손잡이인지가 주어졌을 때, 각 번호를 누른 엄지손가락이 왼손인지 오른손인지 구하는 문제
- 맨 처음 왼손 엄지는 *, 오른손 엄지는 # 위치에서 시작한다
- 엄지손가락을 사용하는 규칙은 다음과 같다
    - 엄지손가락은 상하좌우 4가지 방향으로만 이동할 수 있으며, 키패드 이동 한 칸은 거리 1에 해당한다
    - 왼쪽 열의 3개의 숫자 1, 4, 7은 왼손 엄지손가락으로 입력한다
    - 오른쪽 열의 3개의 숫자 3, 6, 9는 오른손 엄지손가락으로 입력한다
    - 가운데 열의 4개의 숫자 2, 5, 8, 0은 두 엄지손가락의 현재 키패드의 위치에서 더 가까운 엄지손가락을 사용한다
        - 만약 두 엄지손가락의 거리가 같다면, 오른손잡이는 오른손을, 왼손잡이는 왼손을 사용한다
- numbers 배열의 크기는 1 이상 1,000 이하이며, 원소는 0 이상 9 이하인 정수이다
- hand는 "left" 또는 "right"로, "left"는 왼손잡이, "right"는 오른손잡이를 의미한다
- 왼손 엄지손가락을 사용한 경우는 "L", 오른손 엄지손가락을 사용한 경우는 "R"을 순서대로 이어 붙여 문자열 형태로 리턴한다

Example:
- Input : numbers=[1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], hand="right"
- Output : "LRLLLRLLRRL"

- Input : numbers=[7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], hand="left"
- Output : "LRLLRRLLLRR"

- Input : numbers=[1, 2, 3, 4, 5, 6, 7, 8, 9, 0], hand="right"
- Output : "LLRLLRLLRL"

Note:
편리한 계산을 위해 각 숫자들의 위치를 dict에 저장하여 사용

"""

def solution(numbers, hand):
    location = {1: [0, 0], 2: [0, 1], 3: [0, 2], 4: [1, 0], 5: [1, 1], 6: [1, 2], 7: [2, 0], 8: [2, 1], 9: [2, 2], 0: [3, 1]}
    left, right = [3, 0], [3, 2]
    res = ""

    def get_distance(curr, new):
        return abs(curr[0] - new[0]) + abs(curr[1] - new[1])

    for number in numbers:
        if number in (1, 4, 7):
            left = location[number]
            res += "L"
        elif number in (3, 6, 9):
            right = location[number]
            res += "R"
        else:
            temp = location[number]
            ld, rd = get_distance(left, temp), get_distance(right, temp)
            if ld > rd:
                right = temp
                res += "R"
            elif ld < rd:
                left = temp
                res += "L"
            else:
                if hand == "left":
                    left = temp
                    res += "L"
                else:
                    right = temp
                    res += "R"

    return res