"""

[PCCE 기출문제] 10번 / 데이터 분석 : https://school.programmers.co.kr/learn/courses/30/lessons/250121

2차원 정수 리스트인 데이터가 주어졌을 때, 특정 조건을 만족하는 데이터들을 출력하는 문제
- 데이터는 [코드 번호(code), 제조일(date), 최대 수량(maximum), 현재 수량(remain)]으로 구성되어 있다
- data에서 ext 값이 val_ext보다 작은 데이터만 뽑은 후, sort_by에 해당하는 값을 기준으로 오름차순으로 정렬하여 리턴한다
- 제조일(date)는 yyyymmdd의 형태를 가지며, 올바른 날짜만 주어진다
- 조건을 만족하는 데이터는 항상 한 개 이상 존재한다
- 정렬 기준에 해당하는 값이 서로 같은 경우는 존재하지 않는다

Example:
- Input : data=[[1, 20300104, 100, 80], [2, 20300804, 847, 37], [3, 20300401, 10, 8]], ext="date", val_ext=20300501, sort_by="remain"
- Output : [[3,20300401,10,8],[1,20300104,100,80]]

Note:
dict를 사용하여 ext, sort_by 값을 해당하는 인덱스에 매핑
lambda를 사용하여 filter 및 sort

"""

def solution(data, ext, val_ext, sort_by):
    idxs = {"code": 0, "date": 1, "maximum": 2, "remain": 3}
    ext_idx, sort_by_idx = idxs[ext], idxs[sort_by]

    answer = list(filter(lambda x: x[ext_idx] < val_ext, data))
    answer.sort(key = lambda x: x[sort_by_idx])

    return answer