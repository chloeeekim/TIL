"""

49. Group Anagrams : https://leetcode.com/problems/group-anagrams/

string이 포함된 list가 주어졌을 때, anagram인 string끼리 묶는 문제
- 모든 입력은 lowercase이다
- 출력의 순서는 상관없다

Example:
- Input : ["eat","tea","tan","ate","nat","bat"]
- Output : [["ate","eat","tea"],["nat","tan"],["bat"]]

Note:
dict를 사용하여 이전에 anagram인 string이 있었는지 확인
anagram인지 판별하는 것은 단어를 정렬하여 확인
list는 key가 될 수 없으므로 string으로 join하여서 key로 사용한다
anagram인 단어가 있었던 경우 해당 인덱스에 append
anagram인 단어가 없었던 경우 dict에 추가하고 새롭게 append

"""

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        res = []
        for word in strs :
            sw = ''.join(sorted(word))
            if sw in seen :
                res[seen[sw]].append(word)
            else :
                seen[sw] = len(res)
                res.append([word])
        return res