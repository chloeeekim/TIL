"""

647. Palindromic Substrings : https://leetcode.com/problems/palindromic-substrings/

하나의 문자열이 주어졌을 때, 얼마나 많은 palindromic substring이 존재하는지 찾는 문제
- Palindrome : 회문. 거꾸로 읽었을 때도 제대로 읽었을 때와 동일한 경우
- input string의 길이는 1000을 넘지 않는다

Example:
- Input : "abc"
- Output : 3
- "a", "b", "c"

- Input : "aaa"
- Output :6
- "a", "a", "a", "aa", "aa", "aaa"

Note:
모든 경우의 수를 다 계산하는 방법
reverse 문자열 구하는 법 : [::-1]
참고) 더 효율적으로 해결할 수 있는 방법 찾기

"""

class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        for start in range(len(s)) :
            length = 1
            while start + length <= len(s) :
                temp = s[start:start+length]
                if temp == temp[::-1] :
                    count += 1
                length += 1
        return count