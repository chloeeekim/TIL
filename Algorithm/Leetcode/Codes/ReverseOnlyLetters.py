"""

917. Reverse Only Letters : https://leetcode.com/problems/reverse-only-letters/

문자열 S가 주어졌을 때, 알파벳들만 뒤집는 문제
- 알파벳이 아닌 문자는 해당 위치에 그대로 둔다
- S의 길이는 100 이하이다
- S에 포함되는 문자들은 아스키코드값 33 이상 122 이하이다
- S에 '\'나 '"' 는 포함되지 않는다

Example:
- Input : "ab-cd"
- Output : "dc-ba"

- Input : "a-bC-dEf-ghIj"
- Output : "j-Ih-gfE-dCba"

- Input : "Test1ng-Leet=code-Q!"
- Output : "Qedo1ct-eeLg=ntse-T!"

Note:
two-pointer로 왼쪽과 오른쪽에서 각각 알파벳 문자를 찾아서 서로 교환하는 방식
S 내에 알파벳이 하나도 없는 경우가 있을 수 있어 left, right를 찾을 때 가드를 추가

"""

class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        slist = list(S)
        left, right = 0, len(S)-1
        while left < right:
            while not slist[left].isalpha() and left < len(S)-1:
                left += 1
            while not slist[right].isalpha() and right >= 0:
                right -= 1
            if left < right:
                slist[left], slist[right] = slist[right], slist[left]
                left += 1
                right -= 1
        return ''.join(slist)