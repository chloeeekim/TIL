"""

광고 삽입 : https://school.programmers.co.kr/learn/courses/30/lessons/72414

동영상 재생 시간과 공익광고의 재생 시간, 시청자들이 동영상을 재생했던 구간의 정보가 주어졌을 때, 공익광고가 들어갈 시작 시간을 구하는 문제
- 시청자들의 누적 재생시간이 가장 많이 나오는 곳에 공익광고를 삽입한다
    - 만약 시청자들의 누적 재생시간이 가장 많은 곳이 여러 곳이라면, 그 중에서 가장 빠른 시각을 리턴한다
- 동영상 재생시간 길이 play_time과 공익광고 재생시간 길이 adv_time은 길이 8로 고정된 문자열이다
    - play_time, adv_time은 HH:MM:SS 형식이며, 00:00:01 이상 99:59:59 이하이다
    - 공익광고 재생시간은 동영상 재생시간보다 짧거나 같게 주어진다
- 시청자들이 동영상을 재생했던 구간 정보를 담은 문자열 배열 logs의 크기는 1 이상 300,000 이하이다
    - logs 배열의 각 원소는 시청자의 재생 구간을 나타낸다
    - logs 배열의 각 원소는 길이가 17로 고정된 문자열로, H1:M1:S1-H2:M2:S2 형태이다
        - H1:M1:S1은 시청 시작 시간, H2:M2:S2는 시청이 종료된 시각을 의미한다
        - H1:M1:S1은 H2:M2:S2보다 1초 이상 이전 시각으로 주어진다
        - H1:M1:S1과 H2:M2:S2는 play_time 이내의 시각이다
- 시간을 나타내는 HH, H1, H2의 범위는 00~99, 분을 나타내는 MM, M1, M2의 범위는 00~59, 초를 나타내는 SS, S1, S2의 범위는 00~59이다
    - 잘못된 시각은 입력으로 주어지지 않는다
- 공익광고를 삽입할 시각을 HH:MM:SS 형식의 8자리 문자열로 리턴한다
- 동영상 재생 시간은 재생이 종료된 시각 - 재생이 시작된 시각으로 계산한다

Example:
- Input : play_time="02:03:55", adv_time="00:14:15", logs=["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]
- Output : "01:30:59"

- Input : play_time="99:59:59", adv_time="25:00:00", logs=["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"]
- Output : "01:00:00"

- Input : play_time="50:00:00", adv_time="50:00:00", logs=["15:36:51-38:21:49", "10:14:18-15:36:51", "38:21:49-42:51:45"]
- Output : "00:00:00"

Note:
문자열로 주어진 시각은 초 단위로 변경 (toSeconds)
play_time과 adv_time이 같다면 무조건 0초에 공익 광고를 시작해야 하므로 00:00:00을 리턴
각 log의 start, end 시각에 대해서
1. counts[start]에 +1, counts[end]에 -1을 한다
2. counts[i] = i초부터 i+1초까지의 구간을 포함하는 재생된 구간의 개수로 변경
3. counts[i] = 0초부터 i+1초까지 누적된 재생시간으로 변경
이 경우 i초에서 끝나는 광고의 누적 재생시간은 counts[i] - counts[i - 광고 재생시간]이 되므로,
구간합 알고리즘을 사용하여 최대 누적 재생 구간을 구한다
마지막으로 HH:MM:SS 형태로 변경하여 리턴 (toStr)

"""

def toSeconds(time):
    hh, mm, ss = time.split(":")
    return int(hh) * 3600 + int(mm) * 60 + int(ss)

def toStr(time):
    hh, mm, ss = time // 3600, (time % 3600) // 60, time % 60
    return f"{hh:02d}:{mm:02d}:{ss:02d}"

def solution(play_time, adv_time, logs):
    counts = [0] * 360000
    splay, sadv = toSeconds(play_time), toSeconds(adv_time)
    answer = 0

    if splay == sadv:
        return toStr(answer)

    for log in logs:
        s, e = list(toSeconds(x) for x in log.split("-"))
        counts[s] += 1
        counts[e] -= 1

    for i in range(1, splay+1):
        counts[i] += counts[i-1]
    for i in range(1, splay+1):
        counts[i] += counts[i-1]

    max_time = 0
    for i in range(splay):
        if i < sadv - 1:
            if max_time < counts[i]:
                max_time = counts[i]
                answer = 0
        else:
            if max_time < counts[i] - counts[i - sadv]:
                max_time = counts[i] - counts[i - sadv]
                answer = i - sadv + 1

    return toStr(answer)

