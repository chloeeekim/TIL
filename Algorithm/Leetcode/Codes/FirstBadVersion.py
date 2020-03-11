"""

278. First Bad Version : https://leetcode.com/problems/first-bad-version/

특정 버전 이후로 문제가 발생했다고 할 때, 최초로 문제가 발생한 버전을 찾는 문제
- 1부터 n개의 버전이 존재한다
- bool isBadVersion(version) API를 사용하되 최소로 호출하도록 구현한다

Example:
- Input : n = 5
- call isBadVersion(3) -> false
- call isBadVersion(5) -> true
- call isBadVersion(4) -> true
- Output : 4

Note:
binary search 사용
특정 범위 내의 중간값이 bad version이면 중간값 이하의 버전을, 아니라면 중간값 이상의 버전을 확인

"""

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1 :
            return n
        low, high = 1, n
        while low < high :
            mid = int((low + high) / 2)
            isbad = isBadVersion(mid)
            if isbad :
                high = mid
            else :
                low = mid + 1
        return low