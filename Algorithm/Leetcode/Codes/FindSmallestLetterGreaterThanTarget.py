"""

744. Find Smallest Letter Greater Than Target : https://leetcode.com/problems/find-smallest-letter-greater-than-target/

문자로 이루어진 정렬된 리스트 letters가 주어졌을 때, 가장 먼저 등장하는 target보다 큰 문자를 찾는 문제
- letters와 target은 전부 소문자 알파벳으로 이루어져 있다
- letters는 환형 구조로 되어 있다 (target이 z이고 letters가 [a,b]라면 a를 리턴)
- letters의 길이는 [2,10000] 범위이다

Example:
- Input : letters = ["c", "f", "j"], target = "a"
- Output : "c"

- Input : letters = ["c", "f", "j"], target = "c"
- Output : "f"

- Input : letters = ["c", "f", "j"], target = "g"
- Output : "j"

- Input : letters = ["c", "f", "j"], target = "j"
- Output : "c"

- Input : letters = ["c", "f", "j"], target = "k"
- Output : "c"

Note:
letters를 set으로 바꿔 중복을 제거
리스트를 순회하면서 target보다 큰 값이 있다면 해당 값을 리턴
없는 경우 리스트의 첫 번째 값을 리턴

"""

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        letters = sorted(list(set(letters)))
        for ch in letters:
            if ch > target:
                return ch
        return letters[0]