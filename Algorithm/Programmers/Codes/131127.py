"""

할인 행사 : https://school.programmers.co.kr/learn/courses/30/lessons/131127

마트의 할인 정보와 원하는 제품이 주어졌을 때, 원하는 제품을 모두 할인 받을 수 있는 회원등록 날짜의 총 일수를 구하는 문제
- 마트에서는 일정한 금액을 지불하면 10일 동안 회원 자격을 부여한다
- 마트에서는 회원을 대상으로 매일 한 가지 제품을 할인하는 행사를 하며, 할인하는 제품은 하루에 하나씩만 구매할 수 있다
- 원하는 제품과 수량이 할인하는 날짜와 10일 연속으로 일치하는 경우에 맞춰서 회원가입을 하려 한다
- 원하는 제품을 나타내는 문자열 배열 want와 원하는 제품의 수량을 나타내는 정수 배열 number는 다음과 같다
    - want의 길이는 number의 길이와 동일하며, 1 이상 10 이하이다
    - number의 원소는 1 이상 10 이하이며, number의 원소의 합은 10이다
- 마트에서 할인하는 제품을 나타내는 문자열 배열 discount의 길이는 10 이상 100,000 이하이다
- want와 discount의 원소들은 알파벳 소문자로 이루어진 문자열이다
    - wnat의 원소의 길이와 discount의 원소의 길이는 1 이상 12 이하이다
- 가능한 날이 없으면 0을 리턴한다

Example:
- Input : want=["banana", "apple", "rice", "pork", "pot"], number=[3, 2, 2, 2, 1], discount=["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]
- Output : 3

- Input : want=["apple"], number=[10], discount=["banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana"]
- Output : 0

Note:
10일 범위만큼 discount 배열을 확인하며 할인 받아 구매 가능한 품목의 개수를 카운트
구매 가능한 품목과 원하는 품목의 개수를 비교하는 compare 함수를 생성하여 비교

"""

def compare(number, can):
    for n, c in zip(number, can):
        if n > c:
            return False
    return True

def solution(want, number, discount):
    answer = 0
    name = {name: idx for idx, name in enumerate(want)}
    arr = [0] * len(want)

    for i in range(9):
        if discount[i] in name:
            arr[name[discount[i]]] += 1

    for i in range(len(discount) - 9):
        if discount[i+9] in name:
            arr[name[discount[i+9]]] += 1

        if compare(number, arr):
            answer += 1

        if discount[i] in name:
            arr[name[discount[i]]] -= 1

    return answer