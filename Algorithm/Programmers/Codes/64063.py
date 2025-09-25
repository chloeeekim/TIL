"""

호텔 방 배정 : https://school.programmers.co.kr/learn/courses/30/lessons/64063

고객이 투숙하기 원하는 방 번호들의 목록이 주어졌을 때, 각 고객에게 배정되는 방 번호들을 구하는 문제
- 방 배정은 다음과 같은 규칙에 따라 이루어진다
    - 한 번에 한 명씩 신청한 순서대로 방을 배정한다
    - 고객은 투숙하기 원하는 방 번호를 제출한다
    - 고객이 원하는 방이 비어있다면 즉시 배정한다
    - 고객이 원하는 방이 이미 배정되어 있다면 원하는 방보다 번호가 크면서 비어있는 방 중 가장 번호가 작은 방을 배정한다
- 전체 방 개수 k는 1 이상 10^12 이하인 자연수이다
- 고객들이 원하는 방 번호 배열 room_number의 크기는 1 이상 200,000 이하이다
    - room_number의 각 원소들의 값은 1 이상 k 이하인 자연수이다
    - room_number 배열은 모든 고객이 방을 배정받을 수 있는 경우만 입력으로 주어진다

Example:
- Input : k=10, room_number=[1,3,4,1,3,1]
- Output : [1,3,4,2,5,6]

Note:
효율성 테스트를 통과하기 위해 dict에 다음으로 가능한 빈 방을 저장
효율성 테스트에서 런타임 에러가 발생하여 재귀 호출 제한을 2**31-1로 늘려서 해결

"""

import sys
sys.setrecursionlimit(2**31 - 1)

def solution(k, room_number):
    rooms = {}
    res = []

    for room in room_number:
        res.append(find_empty(room, rooms))
    return res


def find_empty(number, rooms):
    if number not in rooms:
        rooms[number] = number + 1
        return number
    empty = find_empty(rooms[number], rooms)
    rooms[number] = empty + 1
    return empty