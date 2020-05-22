"""

72. Edit Distance : https://leetcode.com/problems/edit-distance/

두 개의 문자열이 주어졌을 때, word1을 word2로 변경하는 최소한의 operation의 횟수를 구하는 문제
- 문자 삽입 / 문자 삭제 / 문자 변경(replace)의 세 가지 operation이 가능하다

Example:
- Input : word1 = "horse", word2 = "ros"
- Output : 3
- horse -> rorse (replace 'h' with 'r') / rorse -> rose (remove 'r') / rose -> ros (remove 'e')

- Input : word1 = "intention", word2 = "execution"
- Output : 5
- intention -> inention (remove 't') / inention -> enention (replace 'i' with 'e') / enention -> exention (replace 'n' with 'x') / exention -> exection (replace 'n' with 'c') / exection -> execution (insert 'u')

Note:
2차원 배열을 사용하여 dp로 해결
word1과 word2의 문자가 동일하면 변경이 없으므로, 이전 값(i-1, j-1)을 그대로 사용
word1과 word2의 문자가 다르면, 이전의 가장 작은 값을 선택하여 +1 (변경)

"""

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        arr = [[0]*(len(word2)+1) for _ in range(len(word1)+1)]
        for i in range(len(word1)+1):
            arr[i][0] = i
        for i in range(len(word2)+1):
            arr[0][i] = i
        for i in range(1, len(word1)+1):
            for j in range(1, len(word2)+1):
                if word1[i-1] == word2[j-1]:
                    arr[i][j] = arr[i-1][j-1]
                else:
                    arr[i][j] = min(arr[i-1][j], arr[i-1][j-1], arr[i][j-1])+1
        return arr[-1][-1]