"""

493. Reverse Pairs : https://leetcode.com/problems/reverse-pairs/

정수로 이루어진 리스트 nums가 주어졌을 때, i < j이며 nums[i] > 2*nums[j]를 만족하는 pair의 개수를 구하는 문제
- 주어지는 리스트의 길이는 50000을 넘지 않는다

Example:
- Input : [1,3,2,3,1]
- Output : 2
- [3,1], [3,1] 두 개의 pair가 존재

- Input : [2,4,3,5,1]
- Output : 3
- [4,1], [3,1], [5,1] 세 개의 pair가 존재

Note:
특정 인덱스가 j일 때, 조건을 만족하는 i의 개수는 정렬된 왼쪽 subarray에 2*nums[j]가 위치하게 되는 인덱스의 이후이다
별도로 생성한 snums를 정렬된 순서로 유지하기 위해 bisect 모듈 사용
pair의 개수를 찾기 위해 bisect_right를 통해 2*nums[j]의 삽입 위치를 파악
snums에는 원소의 값을 삽입하기 위해 insort 메소드를 사용

"""

class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        snums, count = [], 0
        for num in nums:
            count += len(snums)-bisect.bisect_right(snums, num*2)
            bisect.insort(snums, num)
        return count