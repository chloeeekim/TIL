/*

불량 사용자 : https://school.programmers.co.kr/learn/courses/30/lessons/64064

사용자 아이디 목록과 불량 사용자 아이디 목록이 주어졌을 때, 제재 아이디 목록으로 가능한 경우의 수를 구하는 문제
- 불량 사용자 아이디 목록은 사용자 아이디 중 일부 문자를 '*' 문자로 가린 형태이다
    - 가리고자 하는 문자 하나에 '*' 문자 하나를 사용하였고, 아이디 당 최소 하나 이상의 '*' 문자가 사용된다
- 불량 사용자 목록에 매핑된 사용자 아이디를 제재 아이디라고 한다
- 사용자 아이디 목록인 user_id 배열의 크기는 1 이상 8 이하이다
    - user_id 배열의 각 원소의 값은 길이 1 이상 8 이하인 문자열이다
    - 사용자 아이디들은 서로 중복되지 않는다
    - 사용자 아이디는 알파벳 소문자와 숫자로만 이루어져 있다
- 불량 사용자 아이디 목록인 banned_id 배열의 크기는 1 이상 user_id 배열의 크기 이하이다
    - banned_id 배열의 각 원소의 값은 길이 1 이상 8 이하인 문자열이다
    - 불량 사용자 아이디는 알파벳 소문자와 숫자, 가리기 위한 '*' 문자로만 이루어져 있다
    - 불량 사용자 아이디는 '*' 문자를 하나 이상 포함한다
    - 불량 사용자 아이디 하나는 사용자 아이디 중 하나에 해당하고, 같은 사용자 아이디가 중복해서 제재 아이디 목록에 들어가는 경우는 없다
- 제재 아이디 목록을 구했을 때, 아이디들이 나열된 순서와 관계없이 아이디 목록의 내용이 동일하다면 같은 것으로 처리하여 하나로 센다

Example:
- Input : user_id=["frodo", "fradi", "crodo", "abc123", "frodoc"], banned_id=["fr*d*", "abc1**"]
- Output : 2
- 가능한 경우의 수는 ["frodo", "abc123"], ["fradi", "abc123"] 두 가지이다

- Input : user_id=["frodo", "fradi", "crodo", "abc123", "frodoc"], banned_id=["*rodo", "*rodo", "******"]
- Output : 2
- 가능한 경우의 수는 ["frodo", "crodo", "abc123"], ["frodo", "crodo", "frodoc"] 두 가지이다

- Input : user_id=["frodo", "fradi", "crodo", "abc123", "frodoc"], banned_id=["fr*d*", "*rodo", "******", "******"]
- Output : 3
- 가능한 경우의 수는 ["frodo", "crodo", "abc123", "frodoc"], ["fradi", "crodo", "abc123", "frodoc"], ["fradi", "frodo", "abc123", "frodoc"] 세 가지이다

Note:
permutations로 가능한 모든 조합을 구해 banned_id와 매칭되는지 확인한 후 제재 아이디 목록에 추가하는 방식
user_id 및 banned_id의 크기가 최대 8이기 때문에 모든 조합을 검사해도 ok

 */

class Solution {
    fun solution(user_id: Array<String>, banned_id: Array<String>): Int {
        var answer = mutableSetOf<List<String>>()

        fun solve(user: List<String>): Boolean {
            for ((u, b) in user.zip(banned_id)) {
                if (u.length != b.length) return false

                val bRe = Regex(b.replace("*", "."))
                if (!bRe.matches(u)) return false
            }
            return true
        }

        for (perm in permutations(user_id, banned_id.size)) {
            if (solve(perm)) {
                answer.add(perm.sorted())
            }
        }

        return answer.size
    }

    fun permutations(ids: Array<String>, size: Int): List<List<String>> {
        val res = mutableListOf<List<String>>()
        val used = BooleanArray(ids.size)

        fun dfs(path: MutableList<String>) {
            if (path.size == size) {
                res.add(path.toList())
                return
            }
            for (i in ids.indices) {
                if (!used[i]) {
                    used[i] = true
                    path.add(ids[i])
                    dfs(path)
                    path.removeAt(path.lastIndex)
                    used[i] = false
                }
            }
        }

        dfs(mutableListOf())
        return res
    }
}