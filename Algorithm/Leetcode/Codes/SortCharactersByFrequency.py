"""

451. Sort Characters By Frequency : https://leetcode.com/problems/sort-characters-by-frequency/

문자열이 주어졌을 때, 각 문자의 frequency에 따라 정렬하는 문제

Example:
- Input : "tree"
- Output : "eert"
- "eetr" 역시 정답으로 가능

- Input : "cccaaa"
- Output : "cccaaa"
- "aaaccc" 역시 정답으로 가능

- Input : "Aabb"
- Output : "bbAa"
- "bbaA" 역시 정답으로 가능. a와 A는 서로 다른 문자로 취급한다

Note:
dict를 사용하여 해결
특정 문자의 출현 횟수를 seen에 저장하고, 이를 value에 따라 정렬하여 결과 문자열을 만드는 방식

"""

class Solution:
    def frequencySort(self, s: str) -> str:
        seen, res = {}, ""
        for ch in s:
            seen[ch] = 1 if ch not in seen else seen[ch]+1
        for d in sorted(seen.items(), key=(lambda x: x[1]), reverse=True):
            res += d[0]*d[1]
        return res