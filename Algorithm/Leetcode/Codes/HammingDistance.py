"""

461. Hamming Distance : https://leetcode.com/problems/hamming-distance/

주어진 두 개의 정수의 Hamming distance를 구하는 문제
- Hamming distance란 2진수로 나타내었을 때 (비트 단위로) 다른 값의 개수를 의미한다

Example:
- Input : x = 1, y = 4
- Output : 2
- 1 = 0001 이고, 4 = 0100 이므로 두 번째 비트와 네 번째 비트가 서로 다르다

Note:
xor 연산(^)을 사용하여 두 숫자의 비트 차이를 구하는 방식
bin(x)를 함수를 사용하면 이진수를 문자열의 형태로 리턴하므로, '1'의 개수를 count하면 된다

"""

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return bin(x^y).count('1')