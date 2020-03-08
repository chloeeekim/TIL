"""

91. Decode Ways : https://leetcode.com/problems/decode-ways/

숫자로 이루어진 문자열이 주어졌을 때, 해당 문자열을 decode할 수 있는 방법의 가짓수를 구하는 문제
- A-Z는 각각 1부터 26까지의 숫자와 매칭된다
- 주어지는 문자열은 non-empty이며, 숫자로만 이루어진다

Example:
- Input : "12"
- Output : 2
- "AB" (1 2) 혹은 "L" (12)

- Input : "226"
- Output : 3
- "BZ" (2 26) 혹은 "VF" (22 6) 혹은 "BBF" (2 2 6)

Note:
주어진 문자열 s의 특정 인덱스까지 decode가 가능한 가짓수를 구하는 방식
숫자 0에 해당하는 문자는 없으며, 0으로 시작하는 숫자도 문자로 decode할 수 없다
참고) 더 빠른 방법?

"""

class Solution:
    def numDecodings(self, s: str) -> int:
        arr = [0 for _ in range(len(s))]
        for i in range(len(s)) :
            if s[i] != '0' :
                arr[i] += arr[i-1] if i > 0 else 1
            if i > 0 and s[i-1] != '0' :
                num = int(s[i-1] + s[i])
                if num <= 26 :
                    arr[i] += arr[i-2] if i > 1 else 1
        return arr[-1]