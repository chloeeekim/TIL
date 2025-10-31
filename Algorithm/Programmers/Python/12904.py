"""

가장 긴 팰린드롬 : https://school.programmers.co.kr/learn/courses/30/lessons/12904

문자열 s가 주어졌을 때, s의 부분문자열(substring) 중 가장 긴 팰린드롬의 길이를 구하는 문제
- 팰린드롬(palindrome)이란 앞뒤를 뒤집어도 똑같은 문자열을 의미한다
- 문자열 s의 길이는 2,500 이하의 자연수이다
    - 문자열 s는 알파벳 소문자로만 구성된다

Example:
- Input : s="abcdcba"
- Output : 7

- Input : s="abacde"
- Output : 3

Note:
이중 반복문을 통해 모든 부분문자열을 검사하는 방법도 가능하지만, 시간이 조금 더 걸리는 편
투 포인터 방식으로 idx에 대해 palindrome의 길이가 홀수인 경우와 짝수인 경우 두 가지로 구분하여 확인

"""

def solution(s):
    if s == s[::-1]:
        return len(s)

    answer = 0
    for idx in range(len(s)):
        left, right = idx - 1, idx + 1
        len1 = 1
        while left >= 0 and right < len(s):
            if s[left] == s[right]:
                left -= 1
                right += 1
                len1 += 2
            else:
                break

        left, right = idx, idx + 1
        len2 = 0
        while left >= 0 and right < len(s):
            if s[left] == s[right]:
                left -= 1
                right += 1
                len2 += 2
            else:
                break
        answer = max(answer, len1, len2)
    return answer