"""

884. Uncommon Words from Two Sentences : https://leetcode.com/problems/uncommon-words-from-two-sentences/

주어진 두 개의 문자열에서 한 번만 등장하며, 다른 문자열과 중복되지 않는 단어를 찾는 문제
- 결과 리스트의 순서는 중요하지 않다
- 문자열 A와 B의 길이는 200을 넘지 않는다
- 두 문자열 A, B는 공백과 소문자 알파벳으로만 이루어져 있다

Example:
- Input : A = "this apple is sweet", B = "this apple is sour"
- Output : ["sweet","sour"]

- Input : A = "apple apple", B = "banana"
- Output : ["banana"]

Note:
문자열을 공백을 기준으로 나눈 다음, collections의 Counter를 이용하여 개수를 count
문자열 각각을 count하지 않고, 한꺼번에 합쳐서 count하여 한 번만 등장하는 단어만 확인
다른 문자열에의 포함 여부 또한 단어의 count를 통해 확인할 수 있다

"""

from collections import Counter

class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        total, res = Counter(A.split() + B.split()), []
        for temp, count in total.items():
            if count == 1:
                res.append(temp)
        return res