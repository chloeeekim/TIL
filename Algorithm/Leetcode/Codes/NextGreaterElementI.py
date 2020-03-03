"""

496. Next Greater Element I : https://leetcode.com/problems/next-greater-element-i/

숫자로 이루어진 두 array, nums1과 nums2가 주어졌을 때, nums2에서 nums1의 각 숫자 다음으로 큰 숫자를 찾는 문제
- nums1은 nums2의 subset이다
- NGE : nums1의 특정 숫자 x가 nums2에 등장하는 인덱스 이후로 나타나는 처음으로 x보다 큰 숫자
- NGE가 존재하지 않을 경우, -1

Example:
- Input : nums1 = [4,1,2], nums2 = [1,3,4,2]
- Output : [-1,3,-1]

- Input : nums1 = [2,4], nums2 = [1,2,3,4]
- Output : [3,-1]

Note:
nums1의 값들은 순서에 상관없이 등장하므로 빠르게 값을 찾기 위하여 nums2를 확인하면서 NGE를 구한 값을 dict에 저장

"""

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nextelem = {}
        for i, num in enumerate(nums2) :
            if i == len(nums2) - 1 :
                nextelem[num] = -1
            else :
                nextnum = -1
                for j in range(i+1, len(nums2)) :
                    if nums2[j] > num :
                        nextnum = nums2[j]
                        break
                nextelem[num] = nextnum
        res = []
        for num1 in nums1 :
            res.append(nextelem[num1])
        return res