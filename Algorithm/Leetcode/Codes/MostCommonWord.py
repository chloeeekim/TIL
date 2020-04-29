"""

819. Most Common Word : https://leetcode.com/problems/most-common-word/

문장이 하나 주어졌을 때, 가장 많이 등장하는 단어를 찾는 문제
- banned 리스트에 있는 단어는 제외한다
- 단어는 공백과 punctuation으로 구분된다
- punctuation은 무시한다
- case sensitive하지 않으며, 정답은 무조건 소문자 알파벳으로 나타낸다
- 정답은 unique함이 보장된다

Example:
- Input : paragraph = "Bob hit a ball, the hit BALL flew far after it was hit.", banned = ["hit"]
- Output : "ball"

Note:
dict를 사용
case sensitive 하지 않으므로, 전부 lowercase로 변경하고, 마지막 단어의 처리를 위해 공백을 추가
공백이나 punctuation 같이 알파벳이 아닌 경우에는 단어를 구분하고, dict에 count
내림차순으로 정렬 후 banned 리스트에 포함된 단어는 제외하고 가장 처음에 등장하는 단어가 정답

"""

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words, word = {}, ""
        for ch in paragraph.lower()+' ':
            if ch.isalpha():
                word += ch
            elif word:
                words[word] = 1 if word not in words else words[word]+1
                word = ""
        words = sorted(words.items(), key=(lambda x: x[1]), reverse=True)
        for word in words:
            if word[0] not in banned:
                return word[0]