"""

804. Unique Morse Code Words : https://leetcode.com/problems/unique-morse-code-words/

주어진 words에 있는 단어들을 morse 부호로 변경했을 때, 다르게 구분되는 문자열이 몇 개가 존재하는지 확인하는 문제
- words의 길이는 최대 100이다
- 각 words[i]는 [1,12] 길이 범위이다
- words[i]는 lowercase letters로만 이루어져 있다

Example:
- Input : words = ["gin","zen","gig","msg"]
- Output : 2
- "gin" = "zen" = "--...-." / "gig" = "msg" = "--...--."

Note:
각 알파벳에 해당하는 모스 부호를 저장해두고, 중복을 허용치 않는 set을 사용하여 결과를 확인

"""

class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        alphabets = {'a':".-", 'b':"-...", 'c':"-.-.", 'd':"-..", 'e':".", 'f':"..-.", 'g':"--.",
                     'h':"....", 'i':"..", 'j':".---", 'k':"-.-", 'l':".-..", 'm':"--", 'n':"-.",
                     'o':"---", 'p':".--.", 'q':"--.-", 'r':".-.", 's':"...", 't':"-", 'u':"..-",
                     'v':"...-", 'w':".--", 'x':"-..-", 'y':"-.--", 'z':"--.."}
        res = set()
        for word in words :
            morse = ""
            for ch in word :
                morse += alphabets[ch]
            res.add(morse)
        return len(res)