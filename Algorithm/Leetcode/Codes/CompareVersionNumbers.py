"""

165. Compare Version Numbers : https://leetcode.com/problems/compare-version-numbers/

주어진 두 가지 버전을 비교하는 문제
- version1 > version2인 경우 1을 리턴
- version1 < version2인 경우 -1을 리턴
- 두 가지가 동일한 버전인 경우 0을 리턴
- 주어지는 문자열은 non-empty이며, 숫자와 '.'만을 포함한다
- 0은 각 버전의 default revision이다

Example:
- Input : version1 = "0.1", version2 = "1.1"
- Output : -1

- Input : version1 = "1.0.1", version2 = "1"
- Output : 1

- Input : version1 = "7.5.2.4", version2 = "7.5.3"
- Output : -1

- Input : version1 = "1.01", version2 = "1.001"
- Output : 0
- 01과 같이 앞에 나오는 leading zeroes는 무시한다

- Input : version1 = "1.0", version2 = "1.0.0"
- Output : 0
- 0은 각 버전의 default revision이므로, 1.0은 1.0.0과 동일하다

Note:
- Solution 1
'.'을 기준으로 문자열을 나눈 다음, 각 revision을 숫자로 변환하여 직접 비교하는 방식
하위 버전들이 전부 0인 경우는 default revision
- Solution 2
두 버전 중 긴 버전에 맞추어 0을 추가하는 방식
zip 함수를 사용하여 동일한 레벨의 하위 버전을 비교

"""

# Solution 1

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        list1 = [int(x) for x in version1.split('.')]
        list2 = [int(x) for x in version2.split('.')]
        idx = 0
        while idx < len(list1) and idx < len(list2) :
            if list1[idx] == list2[idx] :
                idx += 1
            elif list1[idx] < list2[idx] :
                return -1
            else :
                return 1
        for i in range(idx, len(list1)) :
            if list1[i] != 0 :
                return 1
        for i in range(idx, len(list2)) :
            if list2[i] != 0 :
                return -1
        return 0

# Solution 2

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        list1 = [int(x) for x in version1.split('.')]
        list2 = [int(x) for x in version2.split('.')]
        maxlen = max(len(list1), len(list2))
        if len(list1) < maxlen :
            list1 += [0] * (maxlen - len(list1))
        if len(list2) < maxlen :
            list2 += [0] * (maxlen - len(list2))
        for v1, v2 in zip(list1, list2) :
            if v1 == v2 :
                continue
            elif v1 > v2 :
                return 1
            else :
                return -1
        return 0