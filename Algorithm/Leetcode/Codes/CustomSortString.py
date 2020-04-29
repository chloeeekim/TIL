"""

791. Custom Sort String : https://leetcode.com/problems/custom-sort-string/

문자열 S와 T가 주어졌을 때, T를 S의 순서대로 재배열하는 문제
- S는 custom order로 정렬되어 있으며, 모든 문자는 한 번씩만 등장한다
- S의 길이는 최대 26이며, T의 길이는 최대 200이다
- S와 T 모두 소문자 알파벳으로만 이루어져 있다

Example:
- Input : S = "cba", T = "abcd"
- Output : "cbad"
- d는 S에 없으므로, 어떤 순서로 배열되어도 상관 없다. 즉, "dcba", "cdba", "cbda" 모두 valid

Note:
collections.Counter를 사용하여 T에 포함된 문자의 개수를 count
S에 포함되지 않은 문자들은 어떠한 순서로 배열되어도 상관없으므로,
우선 S에 포함된 문자들을 순서대로 배열한 다음 나머지 문자들은 전부 뒤에다 붙이는 방식으로 해결

"""

from collections import Counter

class Solution:
    def customSortString(self, S: str, T: str) -> str:
        count, res = Counter(T), ""
        for ch in S:
            if ch in count:
                res += ch*count[ch]
                del count[ch]
        for ch, num in count.items():
            res += ch*num
        return res