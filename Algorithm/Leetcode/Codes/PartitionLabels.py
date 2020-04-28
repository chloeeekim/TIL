"""

763. Partition Labels : https://leetcode.com/problems/partition-labels/

소문자로 이루어진 문자열 S가 주어졌을 때, 아래 조건을 만족하는 최대한 많은 partition으로 나누는 문제
- 각 문자는 최대 하나의 part에만 존재하여야 한다
- 각 part의 크기를 리스트의 형태로 리턴
- S의 길이는 [1, 500] 범위이다

Example:
- Input : S = "ababcbacadefegdehijhklij"
- Output : [9,7,8]
- "ababcbaca", "defegde", "hijhklij"로 나눌 수 있다

Note:
dict를 사용하여 해결
seen에는 각 문자가 등장한 마지막 인덱스를 저장
문자열을 확인하면서 등장한 문자의 마지막 인덱스를 확인하여 part의 길이를 정하는 방식

"""

class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        seen = {ch: idx for idx, ch in enumerate(S)}
        res, temp, start = [], 0, 0
        for i, ch in enumerate(S):
            temp = max(temp, seen[ch])
            if temp == i:
                res.append(i-start+1)
                start = i+1
        return res