"""

40. Combination Sum II : https://leetcode.com/problems/combination-sum-ii/

candidate number의 set이 주어졌을 때, 이를 이용해 target number를 만들 수 있는
모든 unique한 combination을 구하는 문제
- candidates 내의 각 숫자는 무조건 한 번만 사용되어야 한다
- target을 포함한 주어지는 모든 숫자는 양의 정수이다
- 결과는 겹치는 combination을 포함해서는 안 된다

Example:
- Input : candidates = [10,1,2,7,6,1,5], target = 8
- Output : [[1,7],[1,2,5],[2,6],[1,1,6]]

- Input : candidates = [2,5,2,1,2], target = 5
- Output : [[1,2,2],[5]]

Note:
getComb() 라는 함수를 만들어서 recursive하게 해결
CombinationSum에서 사용했던 함수에서 약간만 변경
target과 동일한 값이 나오면 해당 combination을 res에 append
target보다 작은 값일 경우, combination에 일단 포함시키고 다음 값을 고려
target보다 큰 값일 경우, 더 이상 진행하는 것이 의미가 없음

"""

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def getComb(self, temp: List[int], tempSum: int, index: int) :
            for i in range(index, len(candidates)) :
                if tempSum + candidates[i] == target :
                    if temp + [candidates[i]] not in res :
                        res.append(temp + [candidates[i]])
                elif tempSum + candidates[i] > target :
                    break
                else :
                    getComb(self, temp+[candidates[i]], tempSum+candidates[i], i+1)
        getComb(self, [], 0, 0)
        return res