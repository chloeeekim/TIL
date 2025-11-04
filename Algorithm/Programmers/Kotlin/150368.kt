/*

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
emoticons의 size만큼 가능한 discount의 조합을 모두 구한다
구해진 discount 조합에 대해 각 user 별로 플러스 서비스 가입 여부 및 결제 금액을 계산

 */

class Solution {
    fun solution(users: Array<IntArray>, emoticons: IntArray): IntArray {
        val size = emoticons.size
        val discountList = getDiscountList(size)

        val answer = IntArray(2)
        for (discount in discountList) {
            var plusUser = 0
            var totalSales = 0
            for ((rate, price) in users) {
                var expenses = 0
                for (i in emoticons.indices) {
                    if (discount[i] < rate) continue

                    expenses += emoticons[i] * (100 - discount[i]) / 100
                    if (expenses >= price) {
                        plusUser++
                        expenses = 0
                        break
                    }
                }
                totalSales += expenses
            }

            if (answer[0] < plusUser) {
                answer[0] = plusUser
                answer[1] = totalSales
            }
            else if (answer[0] == plusUser && answer[1] < totalSales) {
                answer[1] = totalSales
            }
        }

        return answer
    }

    private fun getDiscountList(n: Int): Array<IntArray> {
        val discount = listOf(10, 20, 30, 40)

        if (n <= 0) return arrayOf(intArrayOf())

        val dSize = discount.size
        val size = Math.pow(dSize.toDouble(), n.toDouble()).toInt()
        val result = Array(size) { IntArray(n) }

        for (i in 0 until size) {
            var index = i
            for (j in 0 until n) {
                result[i][j] = discount[index % dSize]
                index /= dSize
            }
        }

        return result
    }
}