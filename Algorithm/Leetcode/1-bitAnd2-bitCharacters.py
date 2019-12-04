"""

717. 1-bit and 2-bit Characters : https://leetcode.com/problems/1-bit-and-2-bit-characters/

0과 1로 이루어진 리스트가 주어졌을 때, 마지막 character가 1-bit character인지 확인하는 문제
- 1-bit character는 '0'으로 표시된다
- 2-bit character는 '10' 혹은 '11'로 표시된다
- 주어진 리스트는 무조건 0으로 끝난다

Example:
- Input : [1,0,0]
- Output : True
- 10 / 0

- Input : [1,1,1,0]
- Output : False
- 11 / 10

Note:
2-bit character는 무조건 1로 시작하므로, bit가 1인 경우 어떤 경우에도 2-bit character
bit가 0이면서 2-bit character에 포함되지 않는 경우에만 1-bit character

"""

class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        idx, length = 0, len(bits) - 1
        while idx <= length :
            if bits[idx] == 1 :
                idx += 2
            else :
                if idx == length :
                    return True
                idx += 1
        return False