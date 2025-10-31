"""

호텔 대실 : https://school.programmers.co.kr/learn/courses/30/lessons/155651

호텔 예약 시각이 주어졌을 때, 필요한 최소 객실의 수를 구하는 문제
- 한 번 사용한 객실은 퇴실 시간을 기준으로 10분간 청소 후 다음 손님들이 사용할 수 있다
- 예약 시각이 문자열 형태로 담긴 2차원 배열 book_time의 길이는 1 이상 1000 이하이다
    - book_time[i]는 ["HH:MM", "HH:MM"]의 형태로, [대실 시작 시간, 대실 종료 시각]을 의미한다
    - 시각은 HH:MM 형태로 24시간 표기법을 따르며, "00:00"부터 "23:59"까지로 주어진다
        - 예약 시간이 자정을 넘어가는 경우는 없으며, 시작 시간은 항상 종료 시각보다 빠르다

Example:
- Input : book_time=[["15:00", "17:00"], ["16:40", "18:20"], ["14:20", "15:20"], ["14:10", "19:20"], ["18:20", "21:20"]]
- Output : 3

- Input : book_time=[["09:10", "10:10"], ["10:20", "12:20"]]
- Output : 1

- Input : book_time=["10:20", "12:30"], ["10:20", "12:30"], ["10:20", "12:30"]]
- Output : 3

Note:
heap을 사용하여 사용 가능한 방이 있는지 확인하는 방식
heap이 비어 있지 않으면서 사용 가능한 방이 있다면 해당 방을 사용하고,
heap이 비어 있거나 사용 가능한 방이 없다면 필요한 방을 1 증가
주어진 시각은 00:00을 기준으로 한 분 단위로 변경하여 계산을 용이하게 한다

"""

import heapq

def calcMin(time):
    hour, minutes = time.split(":")
    return int(hour) * 60 + int(minutes)

def solution(book_time):
    stimes = sorted([[calcMin(x[0]), calcMin(x[1])] for x in book_time], key=lambda x: x[0])
    heap = []

    count = 0
    for start, end in stimes:
        if heap and start >= heap[0]:
            heapq.heappop(heap)
        else:
            count += 1

        heapq.heappush(heap, end + 10)

    return count