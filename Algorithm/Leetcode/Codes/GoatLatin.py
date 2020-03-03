"""

824. Goat Latin : https://leetcode.com/problems/goat-latin/

문자열 S가 주어졌을 때, 이를 "Goat Latin"으로 변경하는 문제
- 단어가 모음(a, e, i, o, u)으로 시작하는 경우, 단어의 끝에 "ma"를 붙인다
- 단어가 자음(모음이 아닌 모든 알파벳)으로 시작하는 경우, 첫 번째 글자를 가장 끝에 붙이고, 그 다음에 "ma"를 붙인다
- 각 단어의 index에 해당하는 길이만큼 단어의 끝에 "a"를 붙인다 (index는 1부터 시작한다)

Example:
- Input : "I speak Goat Latin"
- Output : "Imaa peaksmaaa oatGmaaaa atinLmaaaaa"

- Input : "The quick brown fox jumped over the lazy dog"
- Output : "heTmaa uickqmaaa rownbmaaaa oxfmaaaaa umpedjmaaaaaa overmaaaaaaa hetmaaaaaaaa azylmaaaaaaaaa ogdmaaaaaaaaaa"

Note:
문자열을 공백을 기준으로 split하여 리스트로 해결한 다음 join하는 방법 사용
참고) 주어지는 문자열은 대소문자를 모두 포함한다

"""

class Solution:
    def toGoatLatin(self, S: str) -> str:
        words, vowel = S.split(), ['a','e','i','o','u','A','E','I','O','U']
        res, idx = [], 1
        for word in words :
            if word[0] in vowel :
                word += 'ma'
            else :
                word = word[1:] + word[0] + 'ma'            
            res.append(word + 'a' * idx)
            idx += 1
        return ' '.join(res)