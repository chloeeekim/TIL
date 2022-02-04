"""

953. Verifying an Alien Dictionary : https://leetcode.com/problems/verifying-an-alien-dictionary/

알파벳의 새로운 사전순서가 주어졌을 때, 이에 맞게 정렬되어 있는지 확인하는 문제
- 주어지는 words 및 order는 알파벳 소문자로만 이루어져 있다
- order의 길이는 26이다 (모든 알파벳이 포함된다)

Example:
- Input : words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
- Output : true


- Input : words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
- Output : false

- Input : words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
- Output : false

Note:
order를 각각 숫자에 매핑하여 ordermap을 생성
주어진 words의 문자를 ordermap을 기반으로 숫자로 변경
words를 정렬했을 때, 동일하면 true, 다르다면 false

"""

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        ordermap = {ch: i for i, ch in enumerate(order)}
        words = [[ordermap[ch] for ch in word] for word in words]
        return words == sorted(words)