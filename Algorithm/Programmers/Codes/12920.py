"""

선입 선출 스케줄링 : https://school.programmers.co.kr/learn/courses/30/lessons/12920

처리해야 할 작업량과 각 CPU 코어의 처리 시간이 주어졌을 때, 마지막 작업을 처리하는 코어의 번호를 구하는 문제
- 작업은 동일한 작업이 n개이다
- CPU는 다음과 같은 특징이 있다
    - CPU에는 여러 개의 코어가 있고, 코어별로 한 작업을 처리하는 시간이 다르다
    - 한 코어에서 작업이 끝나면 작업이 없는 코어가 바로 다음 작업을 수행한다
    - 2개 이상의 코어가 남을 경우, 앞의 코어부터 작업을 처리한다
- 처리해야 할 작업의 개수 n은 50,000개를 넘기지 않는다
- 각 코어의 처리시간이 담긴 배열 cores의 길이는 2 이상 10,000 이하이다
    - 코어당 작업을 처리하는 시간은 10,000 이하이다
- 코어의 번호는 1번부터 시작한다

Example:
- Input : n=6, cores=[1, 2, 3]
- Output : 2

Note:
이분탐색으로 모든 작업을 처리하는 데 필요한 시간(t)을 구하고,
t-1초에 완료되는 작업들의 개수를 확인한 뒤, t초에 작업을 할당받는 코어를 찾는 방식

"""

def solution(n, cores):
    lc = len(cores)
    if n <= lc:
        return n

    left, right = 0, max(cores) * n
    while left < right:
        mid = (left + right) // 2
        finish = sum(mid // c for c in cores) + lc
        if finish >= n:
            right = mid
        else:
            left = mid + 1

    finished = sum((left - 1) // c for c in cores) + lc
    for i, c in enumerate(cores):
        if left % c == 0:
            finished += 1
            if finished == n:
                return i + 1

    return 0