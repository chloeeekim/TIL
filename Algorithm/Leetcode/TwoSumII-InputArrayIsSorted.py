"""

167. Two Sum II - Input Array is sorted : https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

주어진 정수 배열에서 두 값의 합이 찾고자 하는 값(target)일 경우,
두 인덱스를 반환하는 문제
- 주어진 정수 배열은 이미 증가하는 방향으로 정렬되어 있다
- 인덱스는 non zero-based로 리턴해야 한다 (1부터 시작)
- 정확히 하나의 솔루션이 존재
- 동일한 값은 두 번 사용할 수 없다

Example:
- Input : nums = [2,7,11,15], target = 9
- Output : [1,2]
- nums[0] + nums[1] = 2 + 7 = 9, index1 = 1, index2 = 2

Note:
dict 사용 (key : 확인한 정수값 / value : 인덱스)

"""

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        temp = {}
        for i, num in enumerate(numbers) :
            if target - num in temp :
                return [temp[target - num] + 1, i + 1]
            else :
                temp[num] = i