"""

344. Reverse String : https://leetcode.com/problems/reverse-string/

리스트의 형태로 주어지는 string을 뒤집는 문제
- in-place로 해결

Example:
- Input : ["h","e","l","l","o"]
- Output : ["o","l","l","e","h"]

- Input : ["H","a","n","n","a","h"]
- Output : ["h","a","n","n","a","H"]

Note:
리스트의 앞과 뒤를 서로 바꿔주는 방법

"""

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        length = len(s)
        for i in range(length // 2):
            s[i], s[length-i-1] = s[length-i-1], s[i]