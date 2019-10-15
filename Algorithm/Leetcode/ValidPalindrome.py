"""

125. Valid Palindrome : https://leetcode.com/problems/valid-palindrome/

주어진 문자열이 Palindrome인지 확인하는 문제
- Palindrome : 회문. 거꾸로 읽었을 때도 제대로 읽었을 때와 동일한 경우
- 문자열 내에서 alphanumeric character를 제외한 나머지 경우는 무시한다

Example:
- Input : "A man, a plan, a canal: Panama"
- Output : true

- Input : "race a car"
- Output : false

Note:
re.sub를 사용하여 alphanumeric이 아닌 모든 경우는 ''로 치환
예시를 확인했을 때, 대소문자를 구분하지 않으므로 lowercase로 변경
리버스 문자열 구하는 법 : [::-1]

"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub('\W', '', s).lower()
        if s[::-1] == s :
            return True
        else :
            return False