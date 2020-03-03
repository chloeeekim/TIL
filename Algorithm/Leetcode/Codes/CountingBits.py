"""

338. Counting Bits : https://leetcode.com/problems/counting-bits/

음수가 아닌 숫자 num이 주어졌을 때, 0부터 num까지의 숫자를 2진법으로 나타냈을 때 1의 갯수를 구하는 문제

Example:
- Input : 2
- Output : [0,1,1]

- Input : 5
- Output : [0,1,1,2,1,2]

Note:
bin(num) : num의 2진수를 문자열의 형태로 반환 (8진수 : oct() / 16진수 : hex())
format(num, 'b')을 써도 2진수로 변환 가능. 'b'를 쓰면 접두어 제외 / '#b'를 쓰면 접두어 포함

"""

class Solution:
    def countBits(self, num: int) -> List[int]:
        res = []
        for i in range(num + 1) :
            res.append(bin(i).count('1'))
        return res