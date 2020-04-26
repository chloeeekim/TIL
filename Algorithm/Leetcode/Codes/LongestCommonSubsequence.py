"""

1143. Longest Common Subsequence : https://leetcode.com/problems/longest-common-subsequence/

두 문자열이 주어졌을 때, 가장 긴 common subsequence의 길이를 구하는 문제
- subsequence란 기존의 문자열에서 순서를 변경하지 않고 문자를 제외하여 만들 수 있는 새로운 문자열을 의미한다
- common subsequence가 존재하지 않는 경우, 0을 리턴

Example:
- Input : text1 = "abcde", text2 = "ace"
- Output : 3
- longest common subsequence는 "ace"

- Input : text1 = "abc", text2 = "abc"
- Output : 3

- Input : text1 = "abc", text2 = "def"
- Output : 0

- Input : text1 = "bsbininm", text2 = "jmjkbkjkv"
- Output : 1

Note:
dp로 해결
718번 문제를 해결한 방법을 continuous 하지 않은 subsequence의 경우에도 계산할 수 있도록 변형
참조하는 arr의 원소 값을 다르게 하여 중복되는 문자의 count를 해결

"""

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        len1, len2 = len(text1), len(text2)
        arr = [[0 for _ in range(len2+1)] for _ in range(len1+1)]
        for i in range(len1-1, -1, -1):
            for j in range(len2-1, -1, -1):
                if text1[i] == text2[j]:
                    arr[i][j] = arr[i+1][j+1]+1
                else:
                    arr[i][j] = max(arr[i+1][j], arr[i][j+1])
        return arr[0][0]