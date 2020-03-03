"""

205. Isomorphic Strings : https://leetcode.com/problems/isomorphic-strings/

두 개의 문자열(s, t)가 주어졌을 때, 두 문자열이 isomorphic인지를 판별하는 문제
- isomorphic : 등장하는 문자들이 다른 문자로 맵핑되었을 때, 동일한 순서로 나열되는 경우
- 두 종류의 다른 문자가 하나의 문자로 맵핑되는 경우는 없다
- 하나의 문자가 자기 자신으로 맵핑되는 경우는 존재한다

Example:
- Input : s = "egg", t = "add"
- Output : true

- Input : s = "foo", t = "bar"
- Output : false

- Input : s = "paper", t = "title"
- Output : true

Note:
- Solution 1
문자열을 나타나는 순서에 따라 숫자로 변환한 문자열을 리턴하는 change()라는 함수를 만들어서 해결
s와 t의 change()의 결과가 동일하다면 두 문자열은 isomorphic하다
- Solution 2
s와 t를 순서대로 비교하는 방법으로, 함수를 사용하지 않음
Solution 1과 속도나 메모리 사용량 측면에서 큰 차이가 없음

"""

# Solution 1
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        def change(self, string: str) -> str:
            seen = {}
            res = ""
            count = 0
            for ch in string:
                if ch in seen :
                    res += seen[ch]
                else :
                    res += str(count)
                    seen[ch] = str(count)
                    count += 1
            return res
        snew = change(self, s)
        tnew = change(self, t)
        return snew == tnew

# Solution 2
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dicts, dictt = {}, {}
        res = True
        counts, countt = 0, 0
        for i in range(len(s)) :
            maps = dicts[s[i]] if s[i] in dicts else -1
            mapt = dictt[t[i]] if t[i] in dictt else -1
            
            if maps != mapt :
                return False
            if maps == -1 :
                dicts[s[i]] = str(counts)
                counts += 1
            if mapt == -1 :
                dictt[t[i]] = str(countt)
                countt += 1
        return res