/*

가장 많이 받은 선물 : https://school.programmers.co.kr/learn/courses/30/lessons/258712

선물을 주고 받은 기록을 바탕으로 규칙대로 다음 달에 선물을 주고받을 때, 선물을 가장 많이 받을 친구가 받을 선물의 수를 구하는 문제
- 두 사람이 선물을 주고 받은 기록이 있다면, 두 사람 사이에 더 많은 선물을 준 사람이 다음 달에 선물을 하나 받는다
- 두 사람이 선물을 주고 받은 기록이 없거나, 주고 받은 수가 같다면 선물 지수가 더 큰 사람이 선물을 하나 받는다
- 선물 지수는 자신이 친구들에게 준 선물의 수에서 받은 선물의 수를 뺀 값이다
- 두 사람의 선물 지수가 같다면 다음 달에 선물을 주고 받지 않는다
- friends는 친구의 이름을 의미하는 알파벳 소문자로 이루어진 길이가 10 이하인 문자열의 리스트로 이루어져 있다
- 이름이 같은 친구는 없다
- gifts는 "A B" 형태의 문자열로, A는 선물을 준 친구의 이름, B는 선물을 받은 친구의 이름이며, 공백 하나로 구분된다
- A와 B가 같은 이름인 경우는 존재하지 않는다

Example:
- Input : friends=["muzi", "ryan", "frodo", "neo"], gifts=["muzi frodo", "muzi frodo", "ryan muzi", "ryan muzi", "ryan muzi", "frodo muzi", "frodo ryan", "neo muzi"]
- Output : 2
- frodo -> muzi / muzi, neo -> ryan / muzi, frodo -> neo 가 되므로, ryan가 neo가 2개의 선물을 받게 되어 가장 많은 선물을 받는다

- Input : friends=["joy", "brad", "alessandro", "conan", "david"], gifts=["alessandro brad", "alessandro joy", "alessandro conan", "david alessandro", "alessandro david"]
- Output : 4
- joy, brad, conan, david -> alessandro / joy, brad, conan -> david 가 되므로, alessandro가 4개의 선물을 받게 되어 가장 많은 선물을 받는다

- Input : friends=["a", "b", "c"], gifts=	["a b", "b a", "c a", "a c", "a c", "c a"]
- Output : 0
- 서로 선물을 주고 받은 수도 같고, 선물 지수도 같으므로 아무도 선물을 받지 못한다

Note:
Map을 사용하여 이름과 인덱스를 매핑
2차원 IntArray인 giftarr를 구성하여 giftarr[give][send]의 형식으로 서로 주고 받은 내역을 저장
2차원 IntArray인 giftnum을 구성하여 giftnum[idx][give, send]의 형식으로 선물 지수를 구하기 위한 값을 따로 저장

 */

class Solution {
    fun solution(friends: Array<String>, gifts: Array<String>): Int {
        val size = friends.size
        val names = friends.withIndex().associate { it.value to it.index }
        val giftarr = Array(size) { IntArray(size) }
        val giftnum = Array(size) { IntArray(2) }

        gifts.forEach {
            val (give, send) = it.split(" ")
            val giveidx = names[give]!!
            val sendidx = names[send]!!

            giftarr[giveidx][sendidx]++
            giftnum[giveidx][0]++
            giftnum[sendidx][1]++
        }

        val answer = IntArray(size)
        for (i in 0 until size) {
            for (j in i+1 until size) {
                val giveToI = giftarr[i][j]
                val giveToJ = giftarr[j][i]

                when {
                    giveToI > giveToJ -> answer[i]++
                    giveToJ > giveToI -> answer[j]++
                    else -> {
                        val diffI = giftnum[i][0] - giftnum[i][1]
                        val diffJ = giftnum[j][0] - giftnum[j][1]
                        when {
                            diffI > diffJ -> answer[i]++
                            diffJ > diffI -> answer[j]++
                        }
                    }
                }
            }
        }

        return answer.maxOrNull() ?: 0
    }
}