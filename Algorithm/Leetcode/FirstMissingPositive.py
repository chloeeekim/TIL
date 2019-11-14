"""

41. First Missing Positive : https://leetcode.com/problems/first-missing-positive/

정렬되지 않은 정수로 이루어진 리스트가 주어졌을 때, 포함되어 있지 않은 가장 작은 양의 정수를 찾는 문제

Example:
- Input : [1,2,0]
- Output : 3

- Input : [3,4,-1,1]
- Output : 2

- Input : [7,8,9,11,12]
- Output : 1

Note:
Hard 문제라서 어렵게 생각했는데 너무 단순한 방법이 통과돼서 의아한 수준
이 코드가 어떻게 97.94%로 통과했는지 의문일 뿐
참고) 파이썬이 아닌 다른 언어로 최적화해서 풀어보기

"""

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        i = 1
        while True :
            if i not in nums :
                return i
            else :
                i += 1