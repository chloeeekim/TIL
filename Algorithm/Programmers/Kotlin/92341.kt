/*

주차 요금 계산 : https://school.programmers.co.kr/learn/courses/30/lessons/92341

주차장 요금표와 차량의 입출차 기록이 주어졌을 때, 차량별로 청구할 주차 요금을 계산하는 문제
- 어떤 차량이 입차된 후에 출차된 기록이 없다면, 23:59에 출차된 것으로 간주한다
- 00:00부터 23:59까지의 입출차 내역을 바탕으로 차량별 누적 주차 시간을 계산하여 요금을 일괄로 정산한다
- 누적 주차 시간이 기본 시간 이하라면, 기본 요금을 청구한다
- 누적 주차 시간이 기본 시간을 초과하면, 기본 요금에 더하여 초과한 시간에 대해서 단위 시간마다 단위 요금을 청구한다
- 초과한 시간이 단위 시간으로 나누어 떨어지지 않으면 올림 처리한다
- 결과는 차량 번호가 작은 자동차부터 차례대로 정수 배열에 담아 리턴한다
- records의 원소는 "시각 차량번호 내역" 형식의 문자열이다
    - 각 항목은 공백 하나로 구분된다
    - 시각은 HH:MM 형식의 길이 5인 문자열이며, 잘못된 시각은 주어지지 않는다
    - 차량번호는 0~9로 구성된 길이 4인 문자열이다
    - 내역은 길이 2 또는 3인 문자열로, IN(입차) 또는 OUT(출차)이다
    - records의 원소들은 시각을 기준으로 오름차순으로 정렬되어 주어진다
    - 주차장에 없는 차량이 출차되는 등 잘못된 입력은 주어지지 않는다

Example:
- Input : fees=[180, 5000, 10, 600], records=["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]
- Output : [14600, 34400, 5000]

- Input : fees=[120, 0, 60, 591], records=["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"]
- Output : [0, 591]

- Input : fees=[1, 461, 1, 10], records=["00:00 1234 IN"]
- Output : [14841]

Note:
String.toMinutes 확장 함수를 정의하여 HH:MM 형식의 문자열을 분으로 변환
recordMap에는 차량의 입차 내역을 관리 (출차 시 map에서 제거)
timeMap에는 차량의 누적 주차 시간을 관리

 */

import kotlin.math.ceil

class Solution {
    fun solution(fees: IntArray, records: Array<String>): IntArray {
        val timeMap = mutableMapOf<String, Int>()
        val recordMap = mutableMapOf<String, Int>()

        for (record in records) {
            val (time, carNum, op) = record.split(" ")
            val timeInt = time.toMinutes()
            when (op) {
                "IN" -> recordMap[carNum] = timeInt
                else -> {
                    val inTime = recordMap.remove(carNum)!!
                    timeMap[carNum] = (timeMap[carNum] ?: 0) + (timeInt - inTime)
                }
            }
        }

        val lastTime = "23:59".toMinutes()
        for ((carNum, inTime) in recordMap) {
            timeMap[carNum] = (timeMap[carNum] ?: 0) + (lastTime - inTime)
        }

        return timeMap.map { (carNum, time) ->
            var fee = fees[1]
            val over = time - fees[0]
            if (over > 0) {
                fee += ceil(over.toDouble() / fees[2]).toInt() * fees[3]
            }
            carNum to fee
        }.sortedBy { it.first }.map { it.second }.toIntArray()
    }

    fun String.toMinutes(): Int {
        val (hh, mm) = split(":").map { it.toInt() }
        return hh * 60 + mm
    }
}