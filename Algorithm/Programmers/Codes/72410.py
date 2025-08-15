"""

신규 아이디 추천 : https://school.programmers.co.kr/learn/courses/30/lessons/72410

입력된 아이디를 규칙에 맞는 새로운 추천 아이디로 변경하는 문제
- 아이디의 규칙은 다음과 같다
    - 아이디의 길이는 3자 이상 15자 이하여야 한다
    - 아이디는 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.) 문자만 사용할 수 있다
    - 단, 마침표(.)는 처음과 끝에 사용할 수 없으며, 연속으로 사용할 수 없다
- 규칙에 맞지 않는 아이디는 다음 과정을 거친다
    - 1. 모든 대문자를 대응되는 소문자로 치환한다
    - 2. 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거한다
    - 3. 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환한다
    - 4. 마침표(.)가 처음이나 끝에 위치한다면 제거한다
    - 5. 빈 문자열이라면, "a"를 대입한다
    - 6. 길이가 16자 이상이라면 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거한다
    - 6-1. 마침표(.)가 끝에 위치한다면 제거한다
    - 7. 길이가 2자 이하라면 마지막 문자를 길이가 3이 될 때까지 반복해서 끝에 붙인다
- new_id에 나타날 수 있는 특수문자는 -_.~!@#$%^&*()=+[{]}:?,<>/로 한정된다

Example:
- Input : new_id="...!@BaT#*..y.abcdefghijklm"
- Output : "bat.y.abcdefghi"

- Input : new_id="z-+.^."
- Output : "z--"

- Input : new_id="=.="
- Output : "aaa"

- Input : new_id="123_.def"
- Output : "123_.def"

- Input : "abcdefghijklmn.p"
- Output : "abcdefghijklmn"

Note:
주어진 방법을 순서대로 구현

"""

def solution(new_id):
    new_id = new_id.lower()
    temp = ""
    for ch in new_id:
        if ch.isalpha() or ch.isdigit() or ch == "-" or ch == "_" or ch == ".":
            temp += ch
    while ".." in temp:
        temp = temp.replace("..", ".")
    temp = temp.strip(".")
    if temp == "":
        temp = "a"
    if len(temp) >= 16:
        temp = temp[:15]
    temp = temp.strip(".")
    if len(temp) <= 2:
        temp += temp[-1] * (3 - len(temp))
    return temp