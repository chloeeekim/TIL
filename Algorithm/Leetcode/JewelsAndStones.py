"""

771. Jewels and Stones : https://leetcode.com/problems/jewels-and-stones/

문자열 S 내에 문자열 J에 포함되어 있는 문자가 몇 개가 있는지 확인하는 문제
- J는 모두 다른 문자로 이루어져 있다
- J와 S는 모두 알파벳으로 이루어져 있다
- 대문자와 소문자는 구분된다
- S와 J의 최대 길이는 50이다

Example:
- Input : J = "aA", S = "aAAbbbb"
- Output : 3

- Input : J = "z", S = "ZZ"
- Output : 0

Note:
- Solution 1
J에 있는 문자가 S 내에 몇 개가 등장하는지 확인하여 더하는 방법
- Solution 2
S를 돌면서 해당 문자가 J에 포함되는지 확인하는 방법

"""

# Solution 1

class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        total = 0
        for ch in J :
            total += S.count(ch)
        return total

# Solution 2

class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        total = 0
        for ch in S :
            total += 1 if ch in J else 0
        return total