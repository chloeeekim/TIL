"""

1108. Defanging an IP Address : https://leetcode.com/problems/defanging-an-ip-address/

IP 주소가 주어졌을 때, 이를 defanged version으로 변경하는 문제
- 모든 "."을 "[.]"으로 치환

Example:
- Input : points = address = "1.1.1.1"
- Output : "1[.]1[.]1[.]1"

- Input : address = "255.100.50.0"
- Output : "255[.]100[.]50[.]0"

Note:
replace 함수를 사용하여 해결

"""

class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace(".", "[.]")