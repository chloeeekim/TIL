"""

345. Reverse Vowels of a String : https://leetcode.com/problems/reverse-vowels-of-a-string/

주어진 문자열의 모음(vowel)만을 뒤집는 문제
- 'y'는 모음으로 판단하지 않는다

Example:
- Input : "hello"
- Output : "holle"

- Input : "leetcode"
- Output : "leotcede"

Note:
앞과 뒤에서 모음을 찾아 서로 바꿔주는 방법
string은 직접 교환이 안되므로 list로 변경하여 교환하고, join하여 리턴하는 방법 사용
참고) 소문자만 포함되었다는 내용이 없다

"""

class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = {x: True for x in ['a','e','i','o','u','A','E','I','O','U']}
        head, tail = 0, len(s)-1
        s = list(s)
        while head < tail :
            while head < tail and s[head] not in vowels :
                head += 1
            while head < tail and s[tail] not in vowels :
                tail -= 1
            if head != tail :
                s[head], s[tail] = s[tail], s[head]
            head += 1
            tail -= 1
        return ''.join(s)