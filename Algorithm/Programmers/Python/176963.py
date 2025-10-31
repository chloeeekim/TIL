"""

추억 점수 : https://school.programmers.co.kr/learn/courses/30/lessons/176963

사진 속 인물들과 인물별 그리움 점수가 주어졌을 때, 사진들의 추억 점수를 구하는 문제
- 추억 점수는 사진 속에 나오는 인물의 그리움 점수의 합이다
    - 그리움 점수가 없는 인물의 경우 0으로 계산한다
- 그리워하는 사람의 이름을 담은 문자열 배열 name과 각 사람별 그리움 점수를 담은 정수 배열 yearning의 길이는 3 이상 100 이하이며, 두 배열의 길이는 같다
    - name의 원소의 길이는 3 이상 7 이하이며, 알파벳 소문자로만 이루어져 있다
    - name에는 중복된 값이 들어가지 않는다
    - yearning의 원소는 1 이상 100 이하이다
    - yearning[i]는 i번째 사람의 그리움 점수를 의미한다
- 각 사진에 찍힌 인물들의 이름을 담은 이차원 문자열 배열 photo의 길이는 3 이상 100 이하이다
    - photo[i]의 길이는 1 이상 100 이하이다
    - photo[i]의 원소(문자열)의 길이는 3 이상 7 이하이다
    - photo[i]의 원소들은 알파벳 소문자로만 이루어져 있으며, 중복된 값이 들어가지 않는다

Example:
- Input : name=["may", "kein", "kain", "radi"], yearning=[5, 10, 1, 3], photo=[["may", "kein", "kain", "radi"],["may", "kein", "brin", "deny"], ["kon", "kain", "may", "coni"]]
- Output : [19, 15, 6]

- Input : name=["kali", "mari", "don"], yearning=[11, 1, 55], photo=[["kali", "mari", "don"], ["pony", "tom", "teddy"], ["con", "mona", "don"]]
- Output : [67, 0, 55]

- Input : name=["may", "kein", "kain", "radi"], yearning=[5, 10, 1, 3], photo=[["may"],["kein", "deny", "may"], ["kon", "coni"]]
- Output : [5, 15, 0]

Note:
각 인물별 yearning을 dict에 저장하여 계산

"""

def solution(name, yearning, photo):
    ndict = {name: score for name, score in zip(name, yearning)}

    res = []
    for p in photo:
        total = 0
        for name in p:
            if name in ndict:
                total += ndict[name]
        res.append(total)

    return res