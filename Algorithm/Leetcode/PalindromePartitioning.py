"""

131. Palindrome Partitioning : https://leetcode.com/problems/palindrome-partitioning/

하나의 문자열 s가 주어졌을 때, 각각의 substring이 전부 palindrome인 형태로 나누는 문제
- Palindrome : 회문. 거꾸로 읽었을 때도 제대로 읽었을 때와 동일한 경우
- 가능한 모든 palindrome partitioning을 구해야 한다

Example:
- Input : "aab"
- Output : [["aa","b"],["a","a","b"]]

Note:
palindrome() 함수를 생성하여 recursive하게 해결
길이별로 substring을 구한 다음 해당 substring이 palindrome인지 확인 후,
palindrome이라면 리스트에 추가하고 남은 문자열로 다시 반복하는 방법

"""

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        def palindrome(self, temp: str, before: List[str]) :
            if not temp :
                res.append(before)
            for i in range(1, len(temp) + 1) :
                sub = temp[:i]
                if sub == sub[::-1] :
                    palindrome(self, temp[i:], before + [temp[:i]])
        palindrome(self, s, [])
        return res