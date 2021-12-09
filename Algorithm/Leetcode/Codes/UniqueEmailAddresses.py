"""

929. Unique Email Addresses : https://leetcode.com/problems/unique-email-addresses/

주어진 이메일 리스트 중에서 unique한 이메일의 개수를 구하는 문제
- @를 기준으로 앞은 local name, 뒤는 domain name으로 구분된다
- local name에 포함된 '.'는 없는 것과 동일하다
- local name에 포함된 '+'의 뒷부분은 무시된다

Example:
- Input : emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
- Output : 2
- "testemail@leetcode.com" and "testemail@lee.tcode.com"

- Input : emails = ["a@leetcode.com","b@leetcode.com","c@leetcode.com"]
- 3

Note:
@를 기준으로 local과 domain을 구분
local에 있는 .는 전부 공백으로 replace
local에 있는 +의 뒷부분은 전부 무시(삭제)
set을 사용하여 동일한 unique한 메일의 개수만 확인

"""

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        ans = set()
        for email in emails:
            local, domain = email.split('@')
            local = ''.join(local.split('.'))
            local = local.split('+')[0]
            ans.add(local+'@'+domain)
        return len(ans)