"""

187. Repeated DNA Sequences : https://leetcode.com/problems/repeated-dna-sequences/

DNA sequence가 주어졌을 때, 길이 10의 여러 번 등장하는 구간을 구하는 문제
- 해당 sequence는 A, C, G, T 네 가지로 이루어진다
- 결과는 어떠한 순서로 제출되어도 상관없다

Example:
- Input : s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
- Output : ["AAAAACCCCC","CCCCCAAAAA"]

- Input : s = "AAAAAAAAAAAAA"
- Output : ["AAAAAAAAAA"]

Note:
dict를 사용하여 해당 문자열이 등장했는지 확인하는 방법
길이가 10으로 고정되어 있으므로 길이 10의 string만 확인하면 된다

"""

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        seq, n = {}, len(s)
        for i in range(n-9):
            if s[i:i+10] not in seq:
                seq[s[i:i+10]] = 0
            seq[s[i:i+10]] += 1
        return [x for x, y in seq.items() if y > 1]