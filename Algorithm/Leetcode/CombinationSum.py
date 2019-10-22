"""

39. Combination Sum : https://leetcode.com/problems/combination-sum/

candidate number의 set이 주어졌을 때, 이를 이용해 target number를 만들 수 있는
모든 unique한 combination을 구하는 문제
- candidates 내의 숫자는 동일한 숫자를 몇 번을 반복해 사용해도 된다
- target을 포함한 주어지는 모든 숫자는 양의 정수이다
- 결과는 겹치는 combination을 포함해서는 안 된다

Example:
- Input : candidates = [2,3,6,7], target = 7
- Output : [[7],[2,2,3]]

- Input : candidates = [2,3,5], target = 8
- Output : [[2,2,2,2],[2,3,3],[3,5]]

Note:
getComb() 라는 함수를 만들어서 recursive하게 해결
target과 동일한 값이 나오면 해당 combination을 res에 append
target보다 작은 값일 경우, combination에 일단 포함시키고 다음 값을 고려
target보다 큰 값일 경우, 더 이상 진행하는 것이 의미가 없음
참고) 문제를 잘 읽자. candidates가 정렬되어 있다는 조건이 없다

"""

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def getComb(self, temp: List[int], tempSum: int, index: int) :
            for i in range(index, len(candidates)) :
                if tempSum + candidates[i] == target :
                    temp = temp + [candidates[i]]
                    res.append(temp)
                elif tempSum + candidates[i] > target :
                    break
                else :
                    getComb(self, temp+[candidates[i]], tempSum+candidates[i], i)
        getComb(self, [], 0, 0)
        return res