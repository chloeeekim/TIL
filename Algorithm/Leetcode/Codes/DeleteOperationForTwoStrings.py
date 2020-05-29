"""

583. Delete Operation for Two Strings : https://leetcode.com/problems/delete-operation-for-two-strings/

두 개의 문자열이 주어졌을 때, 최소 몇 개의 문자를 지워야 두 문자열을 동일하게 만들 수 있는지를 확인하는 문제
- 주어진 문자열들의 길이는 500을 넘지 않는다
- 문자열은 소문자 알파벳으로만 이루어져 있다

Example:
- Input : "sea", "eat"
- Output : 2
- "sea"에서 "s"를 지워 "ea"를 만들고, "eat"에서 "t"를 지워서 "ea"로 만든다

Note:
dp로 해결
두 문자열을 최소한으로 지워서 만들 수 있는 subsequence는 최대 길이의 subsequence이므로
두 문자열로 만들 수 있는 최대 길이의 연속되지 않은 subsequence의 길이를 구하는 방식으로 해결

"""

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        arr = [[0 for _ in range(len(word1)+1)] for _ in range(len(word2)+1)]
        for i in range(1, len(word2)+1):
            for j in range(1, len(word1)+1):
                if word2[i-1] == word1[j-1]:
                    arr[i][j] = arr[i-1][j-1]+1
                else:
                    arr[i][j] = max(arr[i-1][j], arr[i][j-1])
        return len(word1)+len(word2)-2*arr[-1][-1]