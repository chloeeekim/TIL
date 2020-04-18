"""

521. Longest Uncommon Subsequence I : https://leetcode.com/problems/longest-uncommon-subsequence-i/

두 문자열이 주어졌을 때, longest uncommon subsequence의 길이를 구하는 문제
- 존재하지 않는 경우 -1을 리턴

Example:
- Input : a = "aba", b = "cdc"
- Output : 3

- Input : a = "aaa", b = "bbb"
- Output : 3

- Input : a = "aaa", b = "aaa"
- Output : -1

Note:
- Solution 1
모든 경우의 수를 다 계산하는 방법
솔루션을 보고 바보 같았다는 것을 깨달았다. 경우의 수를 좀 더 잘 생각해 볼 것
- Solution 2
주어진 문자열도 그 자체만으로 subsequence가 되므로, 동일한 문자열이 아닌 경우 주어진 문자열이 lus가 된다

"""

# Solution 1

class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        def getlen(x: str, y: str) -> int:
            for i in range(len(x), 0, -1):
                for j in range(len(x)-i+1):
                    if x[j:j+i] not in y:
                        return i
            return -1            
        return max(getlen(a,b), getlen(b,a))

# Solution 2

class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        if a == b:
            return -1
        return max(len(a), len(b))