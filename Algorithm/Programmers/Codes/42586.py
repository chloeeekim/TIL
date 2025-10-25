"""

기능개발 : https://school.programmers.co.kr/learn/courses/30/lessons/42586

작업의 진도와 개발 속도가 주어졌을 때, 각 배포마다 몇 개의 기능이 배포되는지를 구하는 문제
- 각 기능은 진도가 100%일 때 서비스에 반영할 수 있다
- 각 기능의 개발 속도는 모두 다르다
    - 뒤에 있는 기능이 앞에 있는 기능보다 먼저 개발될 수 있다
    - 먼저 개발 완료되었더라도 뒤에 있는 기능은 앞에 있는 기능이 배포될 때 함께 배포된다
- 먼저 배포되어야 하는 순서대로 작업의 진도가 적힌 배열 progresses와 각 작업의 개발 속도가 적힌 배열 speeds의 길이는 100 이하이다
    - 작업 진도는 100 미만의 자연수이다
    - 작업 속도는 100 이하의 자연수이다
- 배포는 하루에 한 번만 할 수 있으며, 하루의 끝에 이루어진다고 가정한다

Example:
- Input : progresses=[93, 30, 55], speeds=[1, 30, 5]
- Output : [2, 1]

- Input : progresses=[95, 90, 99, 99, 80, 99], speeds=[1, 1, 1, 1, 1, 1]
- Output: [1, 3, 2]

Note:
앞에 있는 작업이 완료되는 시점에 진도가 100% 이상인 뒤에 있는 작업들을 함께 카운트

"""

import math

def solution(progresses, speeds):
    answer = []
    idx = 0

    while idx < len(progresses):
        count = 1
        time = math.ceil((100 - progresses[idx]) / speeds[idx])
        idx += 1

        for i in range(idx, len(progresses)):
            if progresses[i] + speeds[i] * time >= 100:
                count += 1
                idx += 1
            else:
                break
        answer.append(count)

    return answer