"""

151. Reverse Words in a String : https://leetcode.com/problems/reverse-words-in-a-string/

문자열이 주어졌을 때, 해당 문자열을 단어 단위로 뒤집는 문제
- 단어(word)란 공백이 아닌 문자들로 이루어진 sequence를 의미한다
- Input은 문자열의 앞이나 뒤에 공백들을 포함할 수 있으나, 결과에는 해당 공백들을 포함해서는 안 된다
- 단어 사이에 존재하는 여러 개의 공백들은 하나로 줄여서 결과에 나타내어야 한다

Example:
- Input : "the sky is blue"
- Output : "blue is sky the"

- Input : "  hello world!  "
- Output : "world! hello"

- Input : "a good   example"
- Output : "example good a"

Note:
split으로 단어들을 나눈 다음, 뒤집어서 join으로 합치는 방법 사용

"""

class Solution:
    def reverseWords(self, s: str) -> str:
        sl = s.split()
        return ' '.join(sl[::-1])