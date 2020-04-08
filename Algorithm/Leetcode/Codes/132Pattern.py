"""

456. 132 Pattern : https://leetcode.com/problems/132-pattern/

주어진 정수 리스트에서 a_i, a_j, a_k가 i<j<k 이면서 a_i < a_k < a_j가 되는 subsequence가 있는지 확인하는 문제
- 리스트의 길이는 15,000 이하이다

Example:
- Input : [1,2,3,4]
- Output : False

- Input : [3,1,4,2]
- Output : True
- 132 pattern sequence는 [1,4,2]

- Input : [-1,3,2,0]
- Output : True
- 132 pattern sequence는 [-1,3,2], [-1,3,0], [-1,2,0]

Note:
stack을 사용하여 해결
해당 인덱스의 이전에 존재하는 최소값을 미리 리스트에 저장하여 비교 횟수 감소
stack에는 해당 인덱스 다음에 나오며 최소값보다 큰 값임이 보장된다
참고) 더 효율적인 방법?

"""

class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        tmp, minval, stack = sys.maxsize, [], []
        for num in nums:
            tmp = min(num, tmp)
            minval.append(tmp)
        for i in range(len(nums)-1, 0, -1):
            if nums[i] > minval[i] :
                while stack and stack[-1] <= minval[i]:
                    stack.pop(-1)
                if stack and stack[-1] < nums[i]:
                    return True
                stack.append(nums[i])
        return False