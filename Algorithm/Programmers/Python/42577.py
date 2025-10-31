"""

전화번호 목록 : https://school.programmers.co.kr/learn/courses/30/lessons/42577

전화번호 목록이 주어졌을 때, 한 번호가 다른 번호의 접두어인 경우가 있는지 확인하는 문제
- 전화번호가 담긴 배열 phone_book의 길이는 1 이상 1,000,000 이하이다
    - 각 전화번호의 길이는 1 이상 20 이하이다
    - 같은 전화번호가 중복해서 들어있지 않다
- 어떤 번호가 다른 번호의 접두어인 경우가 있으면 false를, 그렇지 않으면 true를 리턴한다

Example:
- Input : phone_book=["119", "97674223", "1195524421"]
- Output : false

- Input : phone_book=["123","456","789"]
- Output : true

- Input : phone_book=["12","123","1235","567","88"]
- Output : false

Note:
긴 번호는 짧은 번호의 접두어가 될 수 없으므로,
주어진 전화번호들을 길이를 기준으로 오름차순으로 정렬
전화번호를 앞에서부터 잘라 접두어에 해당하는 번호가 이전에 나왔는지 확인

"""

def solution(phone_book):
    book = set()
    for p in sorted(phone_book, key=lambda x: len(x)):
        for i in range(1, len(p)):
            if p[:i] in book:
                return False
        book.add(p)

    return True