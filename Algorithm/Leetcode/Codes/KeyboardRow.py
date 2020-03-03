"""

500. Keyboard Row : https://leetcode.com/problems/keyboard-row/

단어들의 리스트가 주어졌을 때, 키보드 상에서 한 줄에 있는 알파벳으로만 이루어져 있는 단어를 찾는 문제
- 하나의 character는 여러 번 등장할 수 있다
- 입력으로 주어지는 단어들은 알파벳만 포함한다

Example:
- Input : ["Hello", "Alaska", "Dad", "Peace"]
- Output : ["Alaska", "Dad"]

Note:
각 알파벳별 row를 미리 dict에 저장
이전에 나왔던 알파벳의 row와 다른 경우, 결과 리스트에 append하지 않음
참고) 100% / 100%!

"""

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        rows = {'Q':1, 'W':1, 'E':1, 'R':1, 'T':1, 'Y':1, 'U':1, 'I':1, 'O':1, 'P':1,
                'A':2, 'S':2, 'D':2, 'F':2, 'G':2, 'H':2, 'J':2, 'K':2, 'L':2,
                'Z':3, 'X':3, 'C':3, 'V':3, 'B':3, 'N':3, 'M':3}
        res = []
        for word in words :
            row, inrow = rows[word[0].upper()], True
            for ch in word :
                if rows[ch.upper()] != row :
                    inrow = False
                    break
            if inrow :
                res.append(word)
        return res