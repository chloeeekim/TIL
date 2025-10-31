"""

문자열 압축 : https://school.programmers.co.kr/learn/courses/30/lessons/60057

문자열이 주어졌을 때, 1개 이상 단위로 문자열을 잘라 압축하여 표현한 문자열 중 가장 짧은 것의 길이를 구하는 문제
- 문자열에서 같은 값이 연속해서 나타나는 것을 문자의 개수와 반복되는 값으로 표현하여 압축한다
- 문자가 반복되지 않아 한 번만 나타난 경우 1은 생략한다
- 문자열은 제일 앞에서부터 정해진 길이만큼 잘라야 한다
- 단위대로 자르고 마지막에 남는 문자열은 그대로 붙여준다
- s는 길이 1 이상 1000 이하인 문자열로, 알파벳 소문자로만 이루어져 있다

Example:
- Input : s="aabbaccc"
- Output : 7

- Input : s="ababcdcdababcdcd"
- Output : 9

- Input : s="abcabcdede"
- Output : 8

- Input : s="abcabcabcabcdededededede"
- Output : 14

- Input : "xababcdcdababcdcd"
- Output : 17
- 어떤 식으로 잘라도 문자열이 압축되지 않는다

Note:
s의 길이의 절반 이상의 길이로 자르게 되면 압축되지 않으므로, 그 이상은 확인이 불필요
반복 횟수가 한자리수 이상이 될 수 있으므로 반복 횟수의 길이를 함께 고려하기보다 압축 문자열을 구하는 방식으로 구현

"""

def solution(s):
    res = 9999
    l = len(s)
    if l == 1:
        return 1
    for length in range(1, l//2 + 1):
        ssplit = [s[i:i+length] for i in range(0, l, length)]
        new_str, temp, count = "", "", 0
        for sp in ssplit:
            if temp == sp:
                count += 1
            else:
                new_str += str(count) + temp if count > 1 else temp
                temp = sp
                count = 1
        new_str += str(count) + temp if count > 1 else temp
        res = min(res, len(new_str))
    return res