"""

파일명 정렬 : https://school.programmers.co.kr/learn/courses/30/lessons/17686

숫자가 포함된 파일명들이 주어졌을 때, 숫자를 반영하여 정렬한 파일 목록을 구하는 문제
- 파일은 다음과 같은 규칙으로 정렬한다
    - 파일명은 크게 HEAD, NUMBER, TAIL의 세 부분으로 구성된다
        - HEAD는 숫자가 아닌 문자로 이루어져 있으며, 최소한 한 글자 이상이다
        - NUMBER는 한 글자에서 최대 다섯 글자 사이의 연속된 숫자로 이루어져 있으며, 앞쪽에 0이 올 수 있다
            - 즉, 0부터 99999 사이의 숫자로, 00000이나 0101 등도 가능하다
        - TAIL은 그 나머지 부분으로, 여기에 다시 숫자가 나타날 수도 있으며, 아무 글자도 없을 수 있다
    - 파일명을 세 부분으로 나눈 후, 다음 기준에 따라 정렬한다
        - 우선 HEAD 부분을 기준으로 사전 순으로 정렬한다
            - 이 때, 문자열 비교 시 대소문자 구분은 하지 않는다
        - 파일명의 HEAD 부분이 대소문자 차이 외에는 같을 경우, NUMBER의 숫자 순으로 정렬한다
            - 9 < 10 < 0011 < 012 < 13 < 014 순으로 정렬된다
            - 숫자 앞의 0은 무시되며, 012와 12는 정렬 시에 같은 값으로 처리한다
        - 두 파일의 HEAD 부분과 NUMBER 숫자도 같을 경우, 원래 입력에 주어진 순서를 유지한다
- files는 1000개 이하의 파일명을 포함하는 문자열 배열이다
    - 각 파일명은 100 글자 이하 길이로, 영문 대소문자, 숫자, 공백(" "), 마침표("."), 빼기 부호("-")만으로 이루어져 있다
    - 파일명은 영문자로 시작하며, 숫자를 하나 이상 포함한다
    - 중복된 파일명은 없으나, 대소문자나 숫자 앞부분의 0 차이가 있는 경우는 함께 주어질 수 있다

Example:
- Input : files=["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]
- Output : ["img1.png", "IMG01.GIF", "img02.png", "img2.JPG", "img10.png", "img12.png"]

- Input : files=["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]
- Output : ["A-10 Thunderbolt II", "B-50 Superfortress", "F-5 Freedom Fighter", "F-14 Tomcat"]

Note:
각 파일명에서 HEAD와 NUMBER를 구분 (정렬 시에 TAIL은 필요 없으니 제외)
NUMBER는 앞에 오는 0에 대한 처리와 실제 숫자 순으로 정렬되어야 하므로 int 타입으로 변경
HEAD와 NUMBER도 동일한 경우 기존 입력에 주어진 순서를 유지하여야 하므로 입력 시의 인덱스를 함께 정렬 기준으로 사용

"""

def solution(files):
    filedata = []
    for fidx, file in enumerate(files):
        head, number = "", ""
        for idx, ch in enumerate(file):
            if ch.isdigit():
                if not head:
                    head = file[:idx]
                number += ch
            elif head:
                break
        filedata.append([file, head.lower(), int(number), fidx])

    return [x[0] for x in sorted(filedata, key=lambda x: (x[1], x[2], x[3]))]