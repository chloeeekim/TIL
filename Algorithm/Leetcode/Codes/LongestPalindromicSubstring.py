"""

5. Longest Palindromic Substring : https://leetcode.com/problems/longest-palindromic-substring/

문자열 s가 주어졌을 때, 가장 긴 palindromic substring을 찾는 문제
- s의 최대 길이는 1000을 넘지 않는다

Example:
- Input : "babad"
- Output : "bab"
- "aba" 또한 valid한 답이 될 수 있다

- Input : "cbbd"
- Output : "bb"

Note:
- Solution 1
palindromic한 substring이 되기 위해서는 시작과 끝 문자열이 동일해야 하므로
시작 인덱스에서 동일한 문자를 찾아 해당 범위 내의 substring이 palindrome인지 확인하는 방법
Brute Force 보다는 나은 방법이겠지만 비효율적
- Solution 2
특정 인덱스를 기준으로 양쪽으로 확장시키는 방법
길이가 홀수인 경우와 짝수인 경우 두 가지로 구분하여 확인
Solution 1보다 효율적
참고) Manacher's Algorithm 확인하기

"""    

# Solution 1

class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxlen, maxstr = 0, ''
        for i in range(len(s)) :
            for j in range(i, len(s)) :
                if s[i] == s[j] and j - i + 1 > maxlen :
                    string = s[i:j+1]
                    if string == string[::-1] :
                        maxlen = j - i + 1
                        maxstr = string
        return maxstr

# Solution 2

class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxlen, maxstr, length = 0, '', len(s)
        for i in range(length) :
            top, bottom = i, i
            while bottom >= 0 and top < length :
                if s[bottom] == s[top] :
                    if top - bottom + 1 > maxlen :
                        maxlen = top - bottom + 1
                        maxstr = s[bottom:top+1]
                else :
                    break
                bottom -= 1
                top += 1
            top, bottom = i+1, i
            while bottom >= 0 and top < length :
                if s[bottom] == s[top] :
                    if top - bottom + 1 > maxlen :
                        maxlen = top - bottom + 1
                        maxstr = s[bottom:top+1]
                else :
                    break
                bottom -= 1
                top += 1
        return maxstr