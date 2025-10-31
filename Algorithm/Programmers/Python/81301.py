"""

숫자 문자열과 영단어 : https://school.programmers.co.kr/learn/courses/30/lessons/81301

숫자의 일부 자릿수가 영단어로 바뀐 문자열이 주어졌을 때, 원래 숫자를 구하는 문제
- 숫자의 일부 자릿수가 영단어로 바뀌어졌거나, 혹은 바뀌지 않고 그대로인 문자열 s가 주어진다
- s의 길이는 1 이상 50 이하이며, s가 "zero" 혹은 "0"으로 시작하는 경우는 주어지지 않는다
- return 값이 1 이상 2,000,000,000 이하의 정수가 되는 올바른 입력만 주어진다

Example:
- Input : s="one4seveneight"
- Output : 1478

- Input : s="23four5six7"
- Output : 234567

- Input : s="2three45sixseven"
- Output : 234567

- Input : s="123"
- Output : 123

Note:
dict를 사용하여 영어 단어에 해당하는 숫자를 매핑
replace를 사용하여 영어 단어를 숫자로 변경

"""

def solution(s):
    numbers = {"zero": "0", "one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}
    for eng, num in numbers.items():
        s = s.replace(eng, num)
    return int(s)