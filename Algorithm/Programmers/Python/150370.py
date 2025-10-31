"""

개인정보 수집 유효기간 : https://school.programmers.co.kr/learn/courses/30/lessons/150370

개인정보와 약관이 주어졌을 때, 주어진 날짜를 기준으로 파기해야 할 개인정보 번호들을 구하는 문제
- 모든 달은 28일까지 있다고 가정한다
- today는 "YYY.MM.DD"의 형태로 주어진다
- terms의 원소는 "약관종류 유효기간" 형태로, 공백 하나로 구분된다
- 약관 종류는 A ~ Z 중 알파벳 대문자 하나이며, terms 배열에서 약관 종류는 중복되지 않는다
- 유효기간은 개인정보를 보관할 수 있는 달 수를 나타내는 정수이며, 1 이상 100 이하이다
- privacies[i]는 i+1번 개인정보의 수집 일자와 약관 종류를 나타낸다
- privacies의 원소는 "날짜 약관종류" 형태로, 공백 하나로 구분된다
- 날짜는 "YYYY.MM.DD" 형태이며, today 이전의 날짜만 주어진다
- 모든 날짜는 "YYYY.MM.DD" 형태로 점(.) 하나로 구분되며, MM이나 DD가 한 자릿수인 경우 앞에 0이 붙는다
- 파기해야 할 개인정보가 하나 이상 존재하는 입력만 주어진다

Example:
- Input : today="2022.05.19", terms=["A 6", "B 12", "C 3"], privacies=["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]
- Output : [1, 3]
- 첫 번째 개인정보는 2021년 11월 1일까지 보관 가능하므로 파기
- 두 번째 개인정보는 2022년 6월 28일까지 보관 가능하므로 유지
- 세 번째 개인정보는 2022년 5월 18일까지 보관 가능하므로 파기
- 네 번째 개인정보는 2022년 5월 19일까지 보관 가능하므로 유지

- Input : today="2020.01.01", terms=["Z 3", "D 5"], privacies=["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"]
- Output : [1,4,5]

Note:
YYYY.MM.DD 형태의 문자열을 2000년 1월 1일을 기준으로 몇 일째인지를 계산
개인정보 수집 일자 + 유효기간 * 28일을 today와 비교

"""

def solution(today, terms, privacies):
    term_map = {}
    for term in terms:
        kind, duration = term.split()
        term_map[kind] = int(duration)

    def changeDays(s):
        yy, mm, dd = s.split(".")

        # 2000년 1월 1일을 1로 변환
        days = (int(yy) - 2000) * 28 * 12
        days += (int(mm) - 1) * 28
        days += (int(dd) - 1)

        return days

    today = changeDays(today)
    result = []

    for i, privacy in enumerate(privacies):
        date, term = privacy.split()
        date = changeDays(date)

        duration = term_map[term]
        date += duration * 28
        if date <= today:
            result.append(i+1)

    return result
