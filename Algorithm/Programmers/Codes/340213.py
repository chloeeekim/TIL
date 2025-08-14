"""

[PCCP 기출문제] 1번 / 동영상 재생기 : https://school.programmers.co.kr/learn/courses/30/lessons/340213

동영상의 정보와 사용자 입력이 주어졌을 때, 사용자 입력이 모두 끝난 후의 동영상의 위치를 "mm:ss" 형식으로 구하는 문제
- "prev" 명령: 10초 전으로 이동한다. 만약 현재 위치가 10초 미만인 경우 영상의 처음 위치(0분 0초)로 이동한다
- "next" 명령: 10초 후로 이동한다. 만약 동영상의 남은 시간이 10초 미만일 경우 영상의 마지막 위치로 이동한다
- 오프닝 건너뛰기: 현재 재생 위치가 오프닝 구간(op_start <= 현재 재생위치 <= op_end)인 경우 자동으로 오프닝이 끝나는 위치로 이동한다
- 모든 시간은 "mm:ss" 형식이며, 분, 초가 한 자리일 경우 0을 붙여 두 자리로 나타낸다

Example:
- Input : video_len="34:33", pos="13:00", op_start="00:55", op_end="02:55", commands=["next","prev"]
- Output : "13:00"

- Input : video_len="10:55", pos="00:05", op_start="00:15", op_end="06:55", commands=["prev", "next", "next"]
- Output : "06:55"

- Input : video_len="07:22", pos="04:05", op_start="00:15", op_end="04:07", commands=["next"]
- Output : "04:17"
- 시작 위치인 4분 5초가 오프닝 구간이므로 4분 7초로 이동 -> 10초 후로 이동 -> 4분 17초

Note:
시간 계산을 편하게 하기 위해 "mm:ss" 형식을 시간(sec)으로 변환 (to_sec 함수)
초기 상태 및 각 command 실행 후에 오프닝 구간 여부 확인
결과를 "mm:ss" 형식으로 변환 (to_str 함수)

"""

def solution(video_len, pos, op_start, op_end, commands):
    video_len, pos, op_start, op_end = to_sec(video_len), to_sec(pos), to_sec(op_start), to_sec(op_end)

    if is_in_opening(pos, op_start, op_end):
        pos = op_end

    for command in commands:
        if command == "prev":
            pos = pos - 10 if pos >= 10 else 0
        else:
            pos = pos + 10 if pos + 10 <= video_len else video_len
        if is_in_opening(pos, op_start, op_end):
            pos = op_end

    return to_str(pos)

def to_sec(time):
    m, s = time[:2], time[3:]
    return int(m) * 60 + int(s)

def to_str(time):
    m, s = time // 60, time % 60
    return f"{m:02}:{s:02}"

def is_in_opening(time, op_start, op_end):
    return True if op_start <= time <= op_end else False