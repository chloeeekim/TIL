"""

438. Find All Anagrams in a String : https://leetcode.com/problems/find-all-anagrams-in-a-string/

문자열 s 내에서 문자열 p와 anagram인 부분의 시작 인덱스를 모두 찾는 문제
- 문자열은 모두 소문자 알파벳으로 이루어진다
- s와 p의 길이는 20,100을 넘지 않는다
- 결과의 출력 순서는 상관 없다

Example:
- Input : s = "cbaebabacd", p = "abc"
- Output : [0,6]
- index 0 = "cba", index 6 = "bac"

- Input : s = "abab", p = "ab"
- Output : [0,1,2]
- index 0 = "ab", index 1 = "ba", index 2 = "ab"

Note:
collections를 사용하여 s의 부분문자열과 p의 각 문자의 갯수를 카운트
s의 부분문자열을 매번 카운트하는 것이 비효율적이므로,
추가되는 문자와 없어지는 문자를 추가/삭제하는 방식으로 구현

"""

import collections

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        pcount = collections.Counter(p)
        strlen, s, res = len(p), '-'+s, []
        scount = collections.Counter(s[:strlen])
        for i in range(len(s)-strlen):
            if s[i+strlen] in scount:
                scount[s[i+strlen]] += 1
            else:
                scount[s[i+strlen]] = 1
            scount[s[i]] -= 1
            if scount[s[i]] == 0:
                del scount[s[i]]
            if scount == pcount:
                res.append(i)
        return res