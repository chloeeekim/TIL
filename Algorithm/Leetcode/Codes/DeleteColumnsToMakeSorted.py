"""

944. Delete Columns to Make Sorted : https://leetcode.com/problems/delete-columns-to-make-sorted/

n개의 string으로 이루어진 리스트 strs가 주어졌을 때, 정렬되어 있지 않은 column의 개수를 구하는 문제
- strs 내의 모든 문자열의 길이는 동일하다
- 문자열은 알파벳 소문자로만 이루어진다

Example:
- Input : strs = ["cba","daf","ghi"]
- Output : 1
- 아래에서 'bah'를 삭제하면 된다
cba
daf
ghi

- Input : strs = ["a","b"]
- Output : 0

- Input : strs = ["zyx","wvu","tsr"]
- Output : 3

Note:
column별로 문자열을 재조합하여 정렬한 다음, 원 문자열과 동일한지 확인하는 방법
참고) 더 효율적인 방법?

"""

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        newstrs, count = [], 0
        for i in range(len(strs[0])):
            temp = [row[i] for row in strs]
            newstrs.append(temp)
        for s in newstrs:
            if s != sorted(s):
                count += 1
        return count