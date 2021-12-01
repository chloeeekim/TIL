"""

241. Different Ways to Add Parentheses : https://leetcode.com/problems/different-ways-to-add-parentheses/

expression이 주어졌을 때, 가능한 모든 순서로 연산하는 결과를 찾는 문제
- 결과는 어떤 순서로 제출되어도 상관 없다
- expression의 길이는 1 이상 20 이하이다
- expression에는 +, -, * operator만 포함된다
- 주어지는 모든 숫자는 0 이상 99 이하이다

Example:
- Input : expression = "2-1-1"
- Output : [0,2]
- ((2-1)-1) = 0 
(2-(1-1)) = 2

- Input : expression = "2*3-4*5"
- Output : [-34,-14,-10,-10,10]
- (2*(3-(4*5))) = -34 
((2*3)-(4*5)) = -14 
((2*(3-4))*5) = -10 
(2*((3-4)*5)) = -10 
(((2*3)-4)*5) = 10

Note:
recursive하게 해결
operator가 등장할 때마다 각각 왼쪽과 오른쪽 expression의 결과를 구하여 연산을 취한다

"""

class Solution:
    def diffWaysToCompute(self, input: str) -> List[int]:
        if input.isdigit():
            return [int(input)]
        ans = []
        for i in range(len(input)):
            if input[i] in "-+*":
                left = self.diffWaysToCompute(input[:i])
                right = self.diffWaysToCompute(input[i+1:])
                for l in left:
                    for r in right:
                        if input[i] == '-':
                            ans.append(l-r)
                        elif input[i] == '+':
                            ans.append(l+r)
                        else:
                            ans.append(l*r)
        return ans