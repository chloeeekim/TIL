/*

의상 : https://school.programmers.co.kr/learn/courses/30/lessons/42578

의상들의 정보가 주어졌을 때, 서로 다른 옷의 조합의 수를 구하는 문제
- 다음과 같은 방식으로 옷을 조합하여 입을 수 있다
    - 각 종류별로 최대 1가지 의상만 착용할 수 있다
    - 착용한 의상의 일부가 겹치더라도, 다른 의상이 겹치지 않거나, 혹은 의상을 추가로 더 착용한 경우 다른 방법인 것으로 계산한다
    - 하루에 최소 한 개의 의상은 입는다
- 의상들이 담긴 2차원 배열 clothes의 길이는 1 이상 30 이하이다
    - clothes의 각 행은 [의상의 이름, 의상의 종류]로 이루어져 있다
    - 같은 이름을 가진 의상은 존재하지 않는다
    - clothes의 모든 원소는 문자열로 이루어져 있다
    - 모든 문자열의 길이는 1 이상 20 이하인 자연수이고, 알파벳 소문자 또는 '_'로만 이루어져 있다

Example:
- Input : clothes=[["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
- Output : 5

- Input : clothes=[["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]
- Output : 3

Note:
A 종류의 옷이 2가지, B 종류의 옷이 1가지가 있다면, 가능한 모든 경우의 수는 (2 + 1) * (1 + 1) = 6가지이다
가능한 모든 경우의 수에서 아무것도 입지 않는 경우의 수(1)를 제외하는 방식

 */

class Solution {
    fun solution(clothes: Array<Array<String>>): Int {
        val cMap = mutableMapOf<String, Int>()
        for ((name, kind) in clothes) {
            cMap[kind] = cMap.getOrPut(kind) { 0 } + 1
        }

        return cMap.values.fold(1) { acc, i -> acc * (i + 1) } - 1
    }
}