/*

단어 변환 : https://school.programmers.co.kr/learn/courses/30/lessons/43163

두 개의 단어 begin, target과 단어의 집합이 주어졌을 때, 최소 몇 단계의 과정을 거쳐 begin을 target으로 변환할 수 있는지 구하는 문제
- 단어는 다음과 같은 규칙을 이용하여 변환한다
    - 한 번에 한 개의 알파벳만 바꿀 수 있다
    - words에 있는 단어로만 변환할 수 있다
- 각 단어는 알파벳 소문자로만 이루어져 있다
- 각 단어의 길이는 3 이상 10 이하이며, 모든 단어의 길이는 동일하다
- 단어의 집합 words의 길이는 3 이상 50 이하이며, 중복되는 단어는 없다
- begin과 target은 같지 않다
- 변환할 수 없는 경우 0을 리턴한다

Example:
- Input : begin="hit", target="cog", words=["hot", "dot", "dog", "lot", "log", "cog"]
- Output : 4
- "hit" -> "hot" -> "dot" -> "dog" -> "cog"와 같이 4단계를 거쳐 변환 가능하다

- Input : begin="hit", target="cog", words=["hot", "dot", "dog", "lot", "log"]
- Output : 0
- target인 "cog"가 words 안에 없으므로 변환할 수 없다

Note:
queue를 사용하여 bfs 방식으로 해결
이미 변환에 사용한 단어로 다시 변환하는 것은 의미 없으므로, used 배열을 두어 이미 사용한 단어는 사용하지 않도록 함

 */

class Solution {
    data class Elem(val curr: String, val depth: Int, val used: List<Int>)

    fun solution(begin: String, target: String, words: Array<String>): Int {
        if (target !in words) return 0

        val wordLen = begin.length
        val queue = ArrayDeque<Elem>().apply { addLast(Elem(begin, 0, listOf())) }
        var answer = mutableListOf<Int>()

        while (queue.isNotEmpty()) {
            val (curr, depth, used) = queue.removeFirst()
            if (curr == target) {
                answer.add(depth)
                continue
            }

            for ((idx, word) in words.withIndex()) {
                if (idx in used) continue
                if (curr.zip(word).count { (c, w) -> c == w } == wordLen - 1) {
                    queue.addLast(Elem(word, depth + 1, used + idx))
                }
            }
        }

        return answer.minOrNull() ?: 0
    }
}