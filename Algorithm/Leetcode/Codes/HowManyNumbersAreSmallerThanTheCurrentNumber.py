"""

1365. How Many Numbers Are Smaller Than the Current Number : https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/

정수로 이루어진 리스트 nums가 주어졌을 때, j != i이며 nums[j] < nums[i]인 j의 개수를 찾는 문제
- 주어진 리스트의 길이는 2 이상 500 이하이다
- 리스트에 포함된 숫자의 범위는 0 이상 100 이하이다

Example:
- Input : nums = [8,1,2,2,3]
- Output : [4,0,1,1,3]

- Input : nums = [6,5,4,8]
- Output : [2,1,0,3]

- Input : nums = [7,7,7,7]
- Output : [0,0,0,0]

Note:
해당 인덱스의 값보다 작은 값의 개수를 구하면 된다
주어진 리스트를 정렬하였을 때, 해당 값이 처음 등장하는 인덱스가 작은 값의 개수가 된다
정렬된 리스트에서 인덱스를 검색하므로, bisect 모듈을 사용하여 속도를 향상
참고) 다른 방법?

"""

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        snums = sorted(nums)
        return [bisect.bisect_left(snums, num) for num in nums]