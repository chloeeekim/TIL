"""

811. Subdomain Visit Count : https://leetcode.com/problems/subdomain-visit-count/

웹사이트의 도메인과 방문한 카운트 숫자가 주어졌을 때, 각 서브도메인을 몇 번 방문했는지 구하는 문제
- "discuss.leetcode.com"이라는 도메인에 방문하는 경우, "leetcode.com"과 "com" 도메인에도 함께 방문하는 것으로 카운트
- count-paired domain은 방문 횟수와 도메인이 공백 하나를 두고 문자열의 형태로 주어진다
- cpdomains의 길이는 100을 넘지 않는다
- 각 도메인의 길이는 100을 넘지 않는다
- 각 주소는 1개 혹은 2개의 '.' 문자가 포함되어 있다
- 주어지는 방문 횟수는 각 도메인 별로 10000을 넘지 않는다
- 결과 리스트의 순서는 상관 없다

Example:
- Input : ["9001 discuss.leetcode.com"]
- Output : ["9001 discuss.leetcode.com","9001 leetcode.com","9001 com"]

- Input : ["900 google.mail.com","50 yahoo.com","1 intel.mail.com","5 wiki.org"]
- Output : ["901 mail.com","50 yahoo.com","900 google.mail.com","5 wiki.org","5 org","1 intel.mail.com","951 com"]

Note:
각 서브도메인 별로 카운트를 dict로 관리
서브도메인은 '.'으로 구분되므로 해당 문자열 내에 '.'이 없으면 최상위 도메인

"""

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        counts = {}
        for cpdomain in cpdomains :
            cpdomain = cpdomain.split()
            count = int(cpdomain[0])
            domain = cpdomain[1]
            idx = 0            
            while idx != -1 :
                if domain in counts :
                    counts[domain] += count
                else :
                    counts[domain] = count
                idx = domain.find('.')
                domain = domain[idx+1:] if idx != -1 else ""
        res = []
        for count in counts.items() :
            res.append(str(count[1]) + ' ' + count[0])
        return res