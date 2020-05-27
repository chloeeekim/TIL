"""

692. Top K Frequent Words : https://leetcode.com/problems/top-k-frequent-words/

단어들의 리스트가 주어졌을 때, 가장 많이 등장하는 순서대로 k개의 단어를 찾는 문제
- 빈도순으로 가장 높은 단어부터 낮은 단어로 정렬하여 리턴한다
- 두 단어의 빈도가 동일하다면, 알파벳 순서대로 정렬하여 리턴한다
- k는 항상 valid하다고 가정한다
- 주어지는 리스트는 소문자 알파벳만을 포함한다

Example:
- Input : ["i", "love", "leetcode", "i", "love", "coding"], k = 2
- Output : ["i", "love"]
- "i"와 "love"는 동일한 빈도로 등장하므로, 알파벳 순서대로 "i"가 우선한다

- Input : ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k = 4
- Output : ["the", "is", "sunny", "day"]

- Input : ["i", "love", "leetcode", "i", "love", "coding"], k = 3
- Output : ["i","love","coding"]
- "leetcode"와 "coding"은 동일한 빈도로 등장하므로, 알파벳 순서대로 "coding"이 우선한다

Note:
collections.Counter를 사용하여 각 단어별 등장 횟수를 확인
lambda를 사용하여 다중 조건으로 정렬 (빈도순으로 우선 정렬하고, 알파벳 순서로 정렬)

"""

from collections import Counter

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        wcount = sorted(Counter(words).items(), key=lambda x: (-x[1], x[0]))
        return [item[0] for item in wcount[:k]]