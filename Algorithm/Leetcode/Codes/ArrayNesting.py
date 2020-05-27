"""

565. Array Nesting : https://leetcode.com/problems/array-nesting/

0부터 N-1까지의 숫자가 포함된 길이 N의 zero-indexed array가 주어졌을 때, S[i]의 최대 길이를 구하는 문제
- S[i]란 A[i]가 포함된 경우, A[A[i]]도 포함되는 set을 의미한다
- N은 1 이상 20,000 이하이다
- 리스트에 포함된 숫자는 중복이 존재하지 않는다

Example:
- Input : A = [5,4,0,3,1,6,2]
- Output : 4
- S[0] = {A[0], A[5], A[6], A[2]} = {5, 6, 2, 0}

Note:
S에 포함되었는지를 확인하는 arr 리스트를 사용
nums[i]를 S에 포함시킬 때마다 1씩 증가하여 arr에 저장
무조건 circle처럼 첫 인덱스로 되돌아갈 수밖에 없으므로 arr 값이 0이 아닌 경우 S가 완성된 것

"""

class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        arr = [0 for _ in nums]
        for i in range(len(nums)):
            if arr[i] != 0:
                continue
            temp, count = i, 0
            while arr[temp] == 0:
                count += 1
                arr[temp] = count
                temp = nums[temp]
        return max(arr)