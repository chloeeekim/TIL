"""

3. Longest Substring Without Repeating Characters : https://leetcode.com/problems/longest-substring-without-repeating-characters/

주어진 문자열에서 문자가 반복되지 않는 최대 길이의 substring의 길이를 구하는 문제
- subsequence가 아닌 substring이어야 한다 (ex. pwwkew에서 pwke는 subsequence)

Example:
- Input : s = "abcabcbb"
- Output : 3
- "abc" -> 3

- Input : s = "bbbbb"
- Output : 1
- "b" -> 1

- Input : s = "pwwkew"
- Output : 3
- "wke" -> 3 (not "pwke")

Note:
dict 사용 (key : 출현한 문자 / value : 인덱스)
sliding window 방식

"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        res = temp = start = 0
        
        for i, ch in enumerate(s) :
            if ch in seen and seen[ch] >= start :
                res = max(res, temp)
                temp = i - seen[ch]
                start = seen[ch] + 1
            else :
                temp += 1
            seen[ch] = i
        return max(res, temp)