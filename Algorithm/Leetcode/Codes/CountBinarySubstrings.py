"""

696. Count Binary Substrings : https://leetcode.com/problems/count-binary-substrings/

binary string s가 주어졌을 때, 0과 1의 개수가 동일하면서 모든 0과 1이 연속적으로 grouped되어 있는 non-empty substring의 개수를 구하는 문제
- 동일한 substring이 존재하는 경우에도 모든 substring의 개수를 구한다
- s는 0과 1로만 이루어져 있다

Example:
- Input : s = "00110011"
- Output : 6
- "0011", "01", "1100", "10", "0011", "01"로 6개가 존재
"00110011" 같은 경우에는 0과 1이 grouped 되어 있지 않으므로 valid하지 않다

- Input : s = "10101"
- Output : 4
- "10", "01", "10", "01"

Note:
0과 1만 존재하기 때문에 이전과 다른 값이면 0에서 1로, 1에서 0으로 변경된 것으로 확인
이전에 등장한 0 혹은 1의 개수와 이후에 등장한 0 혹은 1의 개수 중
적은 개수만큼 valid한 substring이 존재한다

"""

class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        count, prev, cur = 0, 0, 1
        for i in range(1, len(s)):
            if s[i] != s[i-1]:
                count += min(prev, cur)
                prev, cur = cur, 1
            else:
                cur += 1
        return count + min(prev, cur)
