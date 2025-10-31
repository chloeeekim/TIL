"""

[PCCP 기출문제] 3번 / 아날로그 시계 : https://school.programmers.co.kr/learn/courses/30/lessons/250135

초침이 시침 혹은 분침과 겹칠 때마다 알람이 울리는 아날로그 시계가 있을 때, 주어진 시간 범위 동안 알람이 울리는 횟수를 구하는 문제
- 시작 시간 및 종료 시간은 h, m, s로 주어지며, h1시 m1분 s1초부터 h2시 m2분 s2초까지 알림이 울리는 횟수를 계산한다
- 시간이 23시 59분 59초를 초과하여 0시 0분 0초로 돌아가는 경우는 주어지지 않는다
- 0시 정각, 12시 정각에 초침, 시침, 분침이 모두 겹칠 때에는 알람이 한 번만 울린다

Example:
- Input : h1=0, m1=5, s1=30, h2=0, m2=7, s2=0
- Output : 2
- 약 0시 6분 0.501초에 초침과 시침이 겹침 / 약 0시 6분 6.102초에 초침과 분침이 겹침

- Input : h1=12, m1=0, s1=0, h2=12, m2=0, s2=30
- Output : 1
- 12시 0분 0초에 초침, 분침, 시침이 모두 겹침

- Input : h1=0, m1=6, s1=1, h2=0, m2=6, s2=6
- Output : 0

- Input : h1=11, m1=59, s1=30, h2=12, m2=0, s2=0
- Output : 1

- Input : h1=11, m1=58, s1=59, h2=11, m2=59, s2=0
- Output : 1

- Input : h1=1, m1=5, s1=5, h2=1, m2=5, s2=6
- Output : 2

- Input : h1=0, m1=0, s1=0, h2=23, m2=59, s2=59
- Output : 2852

Note:
각도를 계산하여 겹치는지 확인
- 초침은 1초에 6도 이동 / 분침은 1초에 1/10도 이동 / 시침은 1초에 1/120도 이동
0시 정각 등 시침, 분침, 초침이 모두 겹치는 경우는 -1

"""

def solution(h1, m1, s1, h2, m2, s2):
    start = h1 * 3600 + m1 * 60 + s1
    end = h2 * 3600 + m2 * 60 + s2

    count = 0
    if start == 0 or start == 12 * 3600:
        count += 1

    while start < end:
        hour_d = (start / 120) % 360
        min_d = (start / 10) % 360
        sec_d = (start * 6) % 360

        hour_next = ((start + 1) / 120) % 360
        min_next = ((start + 1) / 10) % 360
        sec_next = ((start + 1) * 6) % 360

        hour_next = 360 if hour_next == 0 else hour_next
        min_next = 360 if min_next == 0 else min_next
        sec_next = 360 if sec_next == 0 else sec_next

        if sec_d < hour_d and sec_next >= hour_next:
            count += 1
        if sec_d < min_d and sec_next >= min_next:
            count += 1
        if sec_next == hour_next and sec_next == min_next:
            count -= 1

        start += 1

    return count