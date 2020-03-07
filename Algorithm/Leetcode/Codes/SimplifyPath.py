"""

71. Simplify Path : https://leetcode.com/problems/simplify-path/

Unix style의 absolute path가 주어졌을 때, 이를 canonical path로 변환하는 문제
- . : 현재 디렉터리를 의미
- .. : 상단 디렉터리를 의미
- canonical path는 slash(/)로 시작하여야 하며, 각 디렉터리들은 반드시 하나의 /로 구분된다
- canonical path에서 마지막 디렉터리 이름 뒤에 /는 따라오지 않는다
- canonical path는 absolute path를 표현하는 가장 짧은 문자열이다

Example:
- Input : "/home/"
- Output : "/home

- Input : "/../"
- Output : "/"

- Input: "/home//foo/"
- Output : "/home/foo"

- Input : "/a/./b/../../c/"
- Output : "/c"

- Input : "/a/../../b/../c//.//"
- Output : "/c"

- Input : "/a//b////c/d//././/.."
- Output : "/a/b/c"

Note:
주어진 absolute path를 /를 기준으로 나누고,
나뉘어진 각 디렉터리 이름이나 지시자를 기준으로 canonical path에 들어갈 디렉터리만 구분하여 res 리스트에 추가
최종적으로 res 리스트가 비어있는 경우에도 /는 출력되어야 하므로 빈 문자열을 append

"""

class Solution:
    def simplifyPath(self, path: str) -> str:
        paths, res = path.split('/'), []
        for dirname in paths :
            if not dirname or dirname == '.' :
                continue
            if dirname == '..' :
                if len(res) > 0 : 
                    del res[-1]
            else :
                res.append(dirname)
        if len(res) == 0 :
            res.append('')
        smplpath = ""
        for dirname in res :
            smplpath += '/' + dirname
        return smplpath