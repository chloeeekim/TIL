"""

937. Reorder Data in Log Files : https://leetcode.com/problems/reorder-data-in-log-files/

데이터 로그가 주어졌을 때, 이를 기준에 맞게 새로 정렬하는 문제
- 로그의 타입은 두 종류가 있다: Letter-log, Digit-log
- Letter-log는 identifier를 제외하고 모두 알파벳 소문자로만 이루어져 있다
- Digit-log는 identifier를 제외하고 모두 숫자로만 이루어져 있다
- Letter-log는 모든 Digit-log보다 앞에 위치해야 한다
- Letter-log는 content에 따라 사전순으로 정렬되어야 한다. 만약 동일한 순서라면 identifier의 순서로 정렬된다
- Digit-log는 상대적인 순서를 유지해야 한다
- 모든 로그의 토큰은 하나의 space로 구분된다

Example:
- Input : logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
- Output : ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]

- Input : logs = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]
- Output : ["g1 act car","a8 act zoo","ab1 off key dog","a1 9 2 3 1","zo4 4 7"]

Note:
digit-log는 id를 제외하고 숫자만, letter-log는 id를 제외하고 문자만 포함하므로 첫 번째 토큰을 기준으로 구분
letter-log는 content를 사전순으로 우선 정렬하고, 동일한 경우 첫 번째 토큰(id)을 기준으로 정렬

"""

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        digit = [l for l in logs if l.split()[1].isdigit()]
        letter = [l for l in logs if l.split()[1].isalpha()]
        letter.sort(key = lambda x: (x.split()[1:], x.split()[0]))
        return letter + digit