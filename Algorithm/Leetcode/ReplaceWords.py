"""

648. Replace Words : https://leetcode.com/problems/replace-words/

dictionary와 문자열이 주어졌을 때, 문자열 내의 단어가 dic 내의 단어로 시작하는 경우,
dic의 문자로 변환한 문자열을 리턴하는 문제
- 입력은 모두 lower-case letter로 주어진다

Example:
- Input : dict = ["cat","bat","rat"], sentence = "the cattle was rattled by the battery"
- Output : "the cat was rat by the bat"

Note:
주어진 문자열을 단어 단위로 잘라서(split) 확인
조건에 맞는 경우 해당 element를 dic에 있는 단어로 변경
공백을 포함한 문자열로 join

"""

class Solution:
    def replaceWords(self, dict: List[str], sentence: str) -> str:
        slist = sentence.split()
        for idx, word in enumerate(slist) :
            for d in dict :
                if word.startswith(d) :
                    slist[idx] = d
                    break
        return ' '.join(slist)