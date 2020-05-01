"""

830. Positions of Large Groups : https://leetcode.com/problems/positions-of-large-groups/

문자열 S가 주어졌을 때, large group의 시작과 끝 위치를 모두 찾는 문제
- 동일한 문자가 3번 이상 연속적으로 반복되는 경우 large group으로 간주한다

Example:
- Input : "abbxxxxzzy"
- Output : [[3,6]]

- Input : "abc"
- Output : []

- Input : "abcdddeeeeaabbbcd"
- Output : [[3,5],[6,9],[12,14]]

Note:
문자열을 순회하며 문자가 변경되는 경우에 시작 인덱스를 비교하여 3번 이상 반복된 경우 결과 list에 append
마지막 문자열을 처리하기 위해 주어진 문자열 S에 공백을 추가

"""

class Solution:
    def largeGroupPositions(self, S: str) -> List[List[int]]:
        res, char, start = [], '', 0
        for i, ch in enumerate(S+' '):
            if ch != char:
                if i-start >= 3:
                    res.append([start, i-1])
                char = ch
                start = i
        return res