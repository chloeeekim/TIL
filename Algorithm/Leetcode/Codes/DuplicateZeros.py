"""

1089. Duplicate Zeros : https://leetcode.com/problems/duplicate-zeros/

고정된 길이의 숫자로 이루어진 리스트 arr이 주어졌을 때, 0이 등장하면 두 번씩 반복되도록 리스트를 수정하는 문제
- 남은 원소들은 오른쪽으로 shift한다
- in-place로 해결할 것
- 리스트의 길이는 1 이상 10000 이하이다
- 리스트에 포함된 원소는 0 이상 9 이하이다

Example:
- Input : [1,0,2,3,0,4,5,0]
- Output : [1,0,0,2,3,0,0,4]

- Input : [1,2,3]
- Output : [1,2,3]

Note:
- Solution 1
0을 발견하면 리스트의 오른쪽 부분을 전부 한 칸씩 shift하는 방식
- Solution 2
0을 발견하면 동일한 위치에 0을 추가하고, 마지막 원소를 pop하여 제거하는 방식

"""

# Solution 1
class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        i = 0
        while i < len(arr):
            if arr[i] == 0:
                for j in range(len(arr)-1, i, -1):
                    arr[j] = arr[j-1]
                i += 1
            i += 1

# Solution 2
class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        for i in range(len(arr)-1, -1, -1):
            if arr[i] == 0:
                arr.insert(i, 0)
                arr.pop()