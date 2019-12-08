"""

748. Shortest Completing Word : https://leetcode.com/problems/shortest-completing-word/

주어진 문자열 licensePlate의 문자들을 모두 포함하는 가장 짧은 단어를 words 리스트에서 찾는 문제
- 대소문자는 구분하지 않는다 ("P"와 "p"는 동일한 것으로 취급)
- 하나의 답이 무조건 존재하는 것은 보장된다
- 답이 여러개인 경우, 가장 처음에 나타나는 단어를 리턴
- licensePlate는 동일한 글자가 여러 번 나타날 수 있으며, 나타나는 횟수 역시 고려하여야 한다
- licensePlate는 [1,7] 길이의 문자열이다
- licensePlate는 숫자, 공백, 알파벳(대소문자)으로 구성된다
- words는 [10,1000] 길이의 리스트이다
- 모든 words[i]는 lowercase로 구성되며, [1,15] 길이이다

Example:
- Input : licensePlate = "1s3 PSt", words = ["step","steps","stripe","stepple"]
- Output : "steps"
- 두 개의 s, 하나의 p와 t를 포함하는 가장 짧은 문자열: steps

- Input : licensePlate = "1s3 456", words = ["looks","pest","stew","show"]
- Output : "pest"
- s를 포함하는 가장 짧은 문자열 중에서 가장 먼저 나타나는 단어: pest

Note:
licensePlate를 먼저 확인하여 알파벳이 몇 번 나타났는지를 확인, dict로 관리
words 리스트를 돌면서 dict에 있는 문자들이 모두 포함되는 단어인지 확인
만약 이전에 조건을 만족하는 단어가 있고, 해당 단어의 길이가 현재 단어보다 짧다면 확인할 필요가 없다

"""

class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        dict = {}
        for ch in licensePlate :
            if ch.isalpha():
                ch = ch.lower()
                dict[ch] = 1 if ch not in dict else dict[ch] + 1
        minlen, res = 20, ""
        for word in words :
            if not res and len(word) >= minlen :
                continue
            contain = True
            for ch in dict :
                if word.count(ch) < dict[ch] :
                    contain = False
                    break
            if contain :
                if minlen > len(word) :
                    minlen = len(word)
                    res = word
        return res