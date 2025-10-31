"""

보석 쇼핑 : https://school.programmers.co.kr/learn/courses/30/lessons/67258

진열대에 진열된 보석들의 정보가 주어졌을 때, 모든 보석을 하나 이상 포함하는 가장 짧은 구간을 찾는 문제
- 진열대 번호 순서대로 보석들의 이름이 저장된 배열 gems의 크기는 1 이상 100,000 이하이다
    - gems 배열의 각 원소는 진열대에 나열된 보석을 나타낸다
    - gems 배열에는 1번 진열대부터 진열대 번호 순서대로 보석이름이 차례대로 저장되어 있다
    - gems 배열의 각 원소는 길이가 1 이상 10 이하인 알파벳 대문자로만 구성된 문자열이다
- 모든 보석을 하나 이상 포함하는 가장 짧은 구간의 시작 진열대 번호와 끝 진열대 번호를 배열에 담아 리턴한다
    - 가장 짧은 구간이 여러 개라면 시작 진열대 번호가 가장 작은 구간을 리턴한다

Example:
- Input : gems=["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]
- Output : [3, 7]

- Input : gems=["AA", "AB", "AC", "AA", "AC"]
- Output : [1, 3]

- Input : gems=["XYZ", "XYZ", "XYZ"]
- Output : [1, 1]

- Input : gems=["ZZZ", "YYY", "NNNN", "YYY", "BBB"]
- Output : [1, 5]

Note:
투 포인터 방식으로 해결
[start, end] 구간이 모든 보석을 다 포함한다면 start를 증가시키고,
[start, end] 구간이 모든 보석을 다 포함하지 못한다면 end를 증가시킨다

"""

def solution(gems):
    gem_kind = len(set(gems))
    contains = {gems[0]: 1}
    start, end = 0, 0
    l = len(gems)
    answer = [0, l]

    while start < l and end < l:
        if len(contains) == gem_kind:
            if end - start < answer[1] - answer[0]:
                answer = [start + 1, end + 1]
            else:
                contains[gems[start]] -= 1
                if contains[gems[start]] == 0:
                    del contains[gems[start]]
                start += 1
        else:
            end += 1
            if end >= l:
                break

            if gems[end] in contains:
                contains[gems[end]] += 1
            else:
                contains[gems[end]] = 1

    return answer
