"""

11. Container With Most Water : https://leetcode.com/problems/container-with-most-water/

음수가 아닌 정수로 이루어진 list가 주어졌을 때, 해당 값만큼의 높이가 있는 벽으로 만들 수 있는 가장 큰 직사각형의 크기를 구하는 문제

Example:
- Input : [1,8,6,2,5,4,8,3,7]
- Output : 49

Note:
왼쪽과 오른쪽에서부터 각각 시작하여 직사각형의 크기를 계산
면적이 최대가 되어야 하므로 각 기둥(값)이 큰 쪽을 우선적으로 선택

"""

class Solution:
    def maxArea(self, height: List[int]) -> int:
        res, left, right = 0, 0, len(height) - 1
        while left < right :
            if height[left] < height[right] :
                temp = (right - left) * height[left]
                left += 1
            else :
                temp = (right - left) * height[right]
                right -= 1
            res = max(res, temp)
        return res