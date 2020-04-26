"""

739. Daily Temperatures : https://leetcode.com/problems/daily-temperatures/

매일의 기온이 주어졌을 때, 해당 날짜 이후로 더 따뜻한 날이 며칠 뒤에 나타나는지 구하는 문제
- 더 이상 따뜻한 날이 존재하지 않는 경우 값은 0으로 한다
- 주어지는 리스트의 길이는 [1, 30000] 범위이며, 온도는 [30, 100] 범위이다

Example:
- Input : T = [73, 74, 75, 71, 69, 72, 76, 73]
- Output : [1, 1, 4, 2, 1, 1, 0, 0]

Note:
stack을 사용하여 해결
[기온, 인덱스]의 형태로 stack에 넣어 날짜를 계산
해당 인덱스 이후로 더 따뜻한 날이 없는 경우에는 stack에 이후의 값들을 보관할 필요가 없다

"""

class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        stack, res = [], [0 for _ in T]
        for i in range(len(T)-1, -1, -1):
            while stack:
                temp = stack.pop(-1)
                if temp[0] > T[i]:
                    res[i] = temp[1]-i
                    stack.append(temp)
                    stack.append([T[i], i])
                    break
            if not stack:
                stack.append([T[i], i])
        return res