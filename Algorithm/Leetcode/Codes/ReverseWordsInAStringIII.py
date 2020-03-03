"""

557. Reverse Words in a String III : https://leetcode.com/problems/reverse-words-in-a-string-iii/

문자열이 주어졌을 때, 해당 문자열의 각 단어를 뒤집는 문제
- 단어(word)란 공백이 아닌 문자들로 이루어진 sequence를 의미한다
- 각 단어는 하나의 공백으로만 나누어져 있으며, 불필요한 공백은 존재하지 않는다

Example:
- Input : "Let's take LeetCode contest"
- Output : "s'teL ekat edoCteeL tsetnoc"

Note:
split으로 단어들을 나눈 다음, 각 단어들을 뒤집어서 결과 string에 붙이는 방법

"""

class Solution:
    def reverseWords(self, s: str) -> str:
        slist = s.split()
        res = ""
        for word in slist :
            res += word[::-1]
            res += ' '
        return res[:-1]