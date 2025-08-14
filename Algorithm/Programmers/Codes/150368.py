"""

이모티콘 할인행사 : https://school.programmers.co.kr/learn/courses/30/lessons/150368

이모티콘 할인 행사의 목표를 최대한으로 달성했을 때의 이모티콘 플러스 서비스 가입자 수와 이모티콘 매출액을 구하는 문제
- 이모티콘 플러스 서비스 가입자를 최대한 늘리는 것이 1차 목표
- 이모티콘 판매액을 최대한 늘리는 것이 2차 목표
- n명의 카카오톡 사용자들에게 이모티콘 m개를 할인하여 판매하며, 각 이모티콘의 할인율은 10, 20, 30, 40% 중 하나로 설정된다
- 각 사용자들은 자신의 기준에 따라 일정 비율 이상 할인하는 이모티콘을 모두 구매한다
- 이모티콘 구매 비용의 합이 일정 가격 이상이 된다면, 이모티콘 구매를 모두 취소하고 이모티콘 플러스 서비스에 가입한다
- users의 원소는 [비율, 가격] 형태로, 비율% 이상의 할인이 있는 이모티콘을 모두 구매하며, 가격 이상의 돈을 구매에 사용하게 되면 이모티콘 플러스 서비스에 가입한다

Example:
- Input : users=[[40, 10000], [25, 10000]], emoticons=	[7000, 9000]
- Output : [1, 5400]
- 1번 이모티콘 30% 할인 / 2번 이모티콘 40% 할인

- Input : users=[[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]], emoticons=[1300, 1500, 1600, 4900]
- Output : [4, 13860]
- 1번, 2번, 4번 이모티콘 40% 할인 / 3번 이모티콘 20% 할인

Note:
dfs 방식으로 가능한 discount 조합을 모두 구한다
구해진 discount 조합에 대해 각 user 별로 service 가입 여부 및 결제 금액을 계산

"""

def solution(users, emoticons):
    percentage = [10, 20, 30, 40]
    el = len(emoticons)
    discounts = []

    def get_discount(temp, count):
        if count == el:
            discounts.append(temp[:])
            return

        for p in percentage:
            temp[count] = p
            get_discount(temp, count + 1)
            temp[count] = 0

    get_discount([0] * el, 0)
    result = [0, 0]

    for discount in discounts:
        service, price = 0, 0
        for user in users:
            temp_price = 0
            for i, d in enumerate(discount):
                if d >= user[0]:
                    temp_price += (emoticons[i] * (100 - d)) / 100
                if temp_price >= user[1]:
                    temp_price = 0
                    service += 1
                    break
            price += temp_price
        if service >= result[0]:
            if service == result[0]:
                result[1] = max(result[1], price)
            else:
                result[1] = price
            result[0] = service

    return result
