"""

체육복 : https://school.programmers.co.kr/learn/courses/30/lessons/42862

체육복을 도난 당한 학생들과 여벌의 체육복을 가져온 학생들의 정보가 주어졌을 때, 체육수업을 들을 수 있는 학생의 최댓값을 구하는 문제
- 체육복은 바로 앞 번호나 바로 뒷 번호의 학생에게만 빌려줄 수 있다
- 전체 학생의 수 n은 2명 이상 30명 이하이다
- 체육복을 도난 당한 학생들의 번호가 담긴 배열 lost의 길이는 1 이상 n 이하이며, 중복은 없다
- 여벌의 체육복을 가져온 학생들의 번호가 담긴 배열 reserve의 길이는 1 이상 n 이하이며, 중복은 없다
- 여벌 체육복이 있는 학생만 다른 학생에게 체육복을 빌려줄 수 있다
- 여벌 체육복을 가져온 학생이 체육복을 도난당했을 수 있다
    - 이 경우, 체육복을 하나만 도난당했다고 가정하며, 남은 체육복이 하나이기에 다른 학생에게 체육복을 빌려줄 수 없다

Example:
- Input : n=5, lost=[2, 4], reserve=[1, 3, 5]
- Output : 5

- Input : n=5, lost=[2, 4], reserve=[3]
- Output : 4

- Input : n=3, lost=[3], reserve=[1]
- Output : 2

Note:
여벌의 체육복을 가져왔으나 도난 당한 학생은 교집합을 사용하여 목록에서 제거
greedy 하게 앞 사람에게 체육복을 빌려줄 수 있거나 뒷 사람에게 빌려줄 수 있는지 체크

"""

def solution(n, lost, reserve):
    lost.sort()
    reserve.sort()

    for i in set(lost) & set(reserve):
        lost.remove(i)
        reserve.remove(i)

    for student in reserve:
        if student - 1 in lost:
            lost.remove(student - 1)
        elif student + 1 in lost:
            lost.remove(student + 1)

    return n - len(lost)