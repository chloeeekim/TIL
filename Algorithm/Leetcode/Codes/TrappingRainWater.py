"""

42. Trapping Rain Water : https://leetcode.com/problems/trapping-rain-water/

음수가 아닌 정수로 이루어진 height 리스트가 주어졌을 때, 채워지는 물의 양을 구하는 문제
- 각 bar의 너비는 1로 계산한다

Example:
- Input : [0,1,0,2,1,0,1,3,2,1,2,1]
- Output : 6

Note:
양쪽 끝에서 시작하여 더 높은 bar를 만나면 계속 갱신하는 방식으로 해결
left와 right 중 작은 값에 해당하는 만큼은 무조건 물이 채워진다

"""

class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        left, right, lmax, rmax, res = 0, len(height)-1, height[0], height[-1], 0
        while left < right:
            if height[left] < height[right]:
                left += 1
                if height[left] < lmax:
                    res += lmax-height[left]
                else:
                    lmax = height[left]
            else:
                right -= 1
                if height[right] < rmax:
                    res += rmax-height[right]
                else:
                    rmax = height[right]
        return res