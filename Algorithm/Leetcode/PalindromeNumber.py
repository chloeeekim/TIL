"""

9. Palindrome Number : https://leetcode.com/problems/palindrome-number/

하나의 정수가 주어졌을 때, 해당 정수가 palindrome인지 확인하는 문제
- Palindrome : 회문. 거꾸로 읽었을 때도 제대로 읽었을 때와 동일한 경우

Example:
- Input : 121
- Output : true

- Input : -121
- Output : false
- -121을 거꾸로 읽으면 121-가 되므로 palindrome이 아님

- Input : 10
- Output : false

Note:
reverse 문자열 구하는 법 : [::-1]

"""

class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        if x == x[::-1] :
            return True
        else : 
            return False