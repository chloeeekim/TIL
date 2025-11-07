/*

메뉴 리뉴얼 : https://school.programmers.co.kr/learn/courses/30/lessons/72411

손님들이 주문한 단품메뉴들의 조합이 주어졌을 때, 가장 많이 함께 주문한 단품메뉴 조합을 구하는 문제
- 코스요리 메뉴는 최소 2가지 이상의 단품메뉴로 구성되며, 최소 2명 이상의 손님으로부터 주문된 단품메뉴 조합에 대해서만 포함한다
- orders 배열의 원소는 크기가 2 이상 10 이하인 문자열이며, 각 문자열은 A ~ Z의 알파벳 대문자로 이루어진다
- orders의 원소에는 같은 알파벳이 중복해서 들어있지 않다
- course 배열의 각 원소는 2 이상 10 이하인 자연수가 오름차순으로 정렬되어 있으며, 중복된 값이 존재하지 않는다
- 오름차순으로 정렬된 각 코스요리 메뉴의 구성을 오름차순으로 정렬하여 배열에 담아 리턴한다
- orders와 course 매개변수는 리턴하는 배열의 길이가 1 이상이 되도록 주어진다

Example:
- Input : orders=["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], course=[2, 3, 4]
- Output : ["AC", "ACDE", "BCFG", "CDE"]

- Input : orders=["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], course=[2, 3, 5]
- Output : ["ACD", "AD", "ADE", "CD", "XYZ"]

- Input : orders=["XYZ", "XWY", "WXA"], course=[2, 3, 4]
- Output : ["WX", "XY"]
- 최소 2명 이상의 손님에게서 주문된 구성만 코스요리 후보에 포함되므로, 요리 3개와 4개로 구성된 코스요리는 추가하지 않는다

Note:
필요한 길이의 combinations를 모두 구한 다음, 조건에 맞는 조합을 필터링

 */

class Solution {
    fun solution(orders: Array<String>, course: IntArray): Array<String> {
        val orderCount = mutableMapOf<String, Int>()
        val maxCount = IntArray(course.maxOrNull()!! + 1)
        val lengthSet = course.toSet()

        for (order in orders) {
            val sorder = order.toCharArray().sortedArray()
            val combinations = makeCombinations(sorder, lengthSet)
            for (comb in combinations) {
                val count = orderCount.getOrDefault(comb, 0) + 1
                orderCount[comb] = count
                val len = comb.length
                maxCount[len] = maxOf(maxCount[len], count)
            }
        }

        return course.flatMap { size ->
            val target = maxCount[size]
            orderCount.filter { (comb, count) ->
                count == target && count >= 2 && comb.length == size
            }.keys
        }.sorted().toTypedArray()
    }

    private fun makeCombinations(chars: CharArray, lengths: Set<Int>): List<String> {
        val result = mutableListOf<String>()
        val n = chars.size
        val limit = lengths.maxOrNull() ?: n

        fun dfs(start: Int, depth: Int, path: StringBuilder) {
            if (depth in lengths) result.add(path.toString())
            if (depth == limit) return

            for (i in start until n) {
                path.append(chars[i])
                dfs(i + 1, depth + 1, path)
                path.deleteCharAt(path.lastIndex)
            }
        }

        dfs(0, 0, StringBuilder())

        return result
    }
}