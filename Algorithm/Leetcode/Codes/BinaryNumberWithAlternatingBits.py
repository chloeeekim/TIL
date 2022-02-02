"""

693. Binary Number with Alternating Bits : https://leetcode.com/problems/binary-number-with-alternating-bits/

양의 정수가 주어졌을 때, alternating bits인지 확인하는 문제
- 인접한 두 비트가 항상 다른 값인지 확인

Example:
- Input : n = 5
- Output : true
- 5 -> 101

- Input : n = 7
- Output : false
- 7 -> 111

- Input : n = 11
- Output : false
- 11 -> 1011

Note:
format 함수를 사용하여 binary로 변환한 다음, 이전 비트와 다른지 확인
동일한 비트가 있는 경우 False를 리턴

"""

class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        binary = format(n, 'b')
        for i in range(1, len(binary)):
            if binary[i] == binary[i-1]:
                return False
        return True