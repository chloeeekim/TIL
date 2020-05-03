"""

860. Lemonade Change : https://leetcode.com/problems/lemonade-change/

레모네이드 한 잔의 금액이 $5라고 했을 때, 손님들이 pay한 금액에 대하여 거스름돈을 줄 수 있는지를 확인하는 문제
- 손님 한 명은 무조건 한 잔의 레모네이드를 구매한다
- 돈의 액수는 $5, $10, $20 세 가지 종류이다

Example:
- Input : [5,5,5,10,20]
- Output : true

- Input : [5,5,10]
- Output : true

- Input : [10,10]
- Output : false
- $10짜리 화폐만 소유하고 있으므로 두 번째 손님에게 $5를 거슬러 줄 수 없다

- Input : [5,5,10,10,20]
- Output : false
- $10짜리 화폐 두 장만 소유하고 있으므로, 마지막 손님에게 $15를 거슬러 줄 수 없다

Note:
화폐가 세 종류밖에 없으므로 손님이 주는 돈도 세 종류로 나눌 수 있다
$5를 받은 경우 거슬러 줄 필요가 없으므로 보유하고 있는 돈에 추가
$10을 받은 경우 $5만 거슬러 줄 수 있다
$20을 받은 경우, $10과 $5로 거슬러주거나 $5 세 장으로 거슬러 줄 수 있다

"""

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        collect = {5: 0, 10: 0, 20: 0}
        for bill in bills:
            collect[bill] += 1
            if bill == 10:
                if not collect[5]:
                    return False
                collect[5] -= 1
            elif bill == 20:
                if collect[5] and collect[10]:
                    collect[5] -= 1
                    collect[10] -= 1
                elif collect[5] >= 3:
                    collect[5] -= 3
                else:
                    return False
        return True