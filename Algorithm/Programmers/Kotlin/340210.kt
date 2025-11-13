/*

[PCCP 기출문제] 4번 / 수식 복원하기 : https://school.programmers.co.kr/learn/courses/30/lessons/340210

2 ~ 9진법 중 하나를 사용하는 진법 체계에서 덧셈 및 뺄셈 수식이 주어졌을 때, 결괏값이 지워진 수식들의 결괏값을 채워넣는 문제
- 결괏값이 불확실한 경우 ?를 사용하여 1 + 5 = ? 과 같이 출력한다
- expressions는 "A + B = C" 혹은 "A - B = C" 형태의 문자열이며, 공백 하나로 구분된다
- A, B는 음이 아닌 두자릿수 이하의 정수이다
- C는 알파벳 X(지워짐) 혹은 음이 아닌 세자릿수 이하의 정수이다
- 결괏값이 음수가 되거나 서로 모순되는 수식은 주어지지 않는다

Example:
- Input : expressions=["14 + 3 = 17", "13 - 6 = X", "51 - 5 = 44"]
- Output : ["13 - 6 = 5"]
- 8진법

- Input : expressions=["1 + 1 = 2", "1 + 3 = 4", "1 + 5 = X", "1 + 2 = X"]
- Output : ["1 + 5 = ?", "1 + 2 = 3"]
- 6 ~ 9진법이 가능 / 1 + 5가 6진법일 때는 10, 7 ~ 9진법일 때는 6이 되므로 ?가 된다

- Input : expressions=["10 - 2 = X", "30 + 31 = 101", "3 + 3 = X", "33 + 33 = X"]
- Output : ["10 - 2 = 4", "3 + 3 = 10", "33 + 33 = 110"]

- Input : expressions=["2 - 1 = 1", "2 + 2 = X", "7 + 4 = X", "5 - 5 = X"]
- Output : ["2 + 2 = 4", "7 + 4 = ?", "5 - 5 = 0"]

- Input : ["2 - 1 = 1", "2 + 2 = X", "7 + 4 = X", "8 + 4 = X"]
- Output : ["2 + 2 = 4", "7 + 4 = 12", "8 + 4 = 13"]

Note:
수식에 포함된 숫자들을 바탕으로 가능한 최소 진법(숫자 6이 포함되었다면 7진법 이상이어야 모순되지 않는다) 계산
결괏값이 지워지지 않은 수식들을 바탕으로 가능한 진법들을 계산 (최소 진법 이상 9진법 이하)
마지막으로 가능한 진법들로 결괏값이 지워진 수식들을 계산하여 결과가 여러 개가 나온다면 ?를, 아니라면 결과를 포함시켜 리턴

 */

class Solution {
    data class Expression(val a: String, val b: String, val op: String, val c: String?)

    fun solution(expressions: Array<String>): Array<String> {
        val known = mutableListOf<Expression>()
        val unknown = mutableListOf<Expression>()
        val nums = mutableSetOf<String>()

        for (exp in expressions) {
            val (a, op, b, e, c) = exp.split(" ")
            if (c == "X") unknown.add(Expression(a, b, op, null))
            else {
                known.add(Expression(a, b, op, c))
                nums.add(c)
            }
            nums.addAll(listOf(a, b))
        }

        val minBase = getMinBase(nums)
        val possibleBases = mutableListOf<Int>()

        for (base in minBase .. 9) {
            var valid = true
            for (exp in known) {
                valid = valid && isValid(exp, base)
                if (!valid) break
            }

            if (valid) possibleBases.add(base)
        }

        return unknown.map { exp ->
            val res = mutableSetOf<String>()
            for (base in possibleBases) {
                res.add(calcLeft(exp, base).toString(base))
            }
            if (res.size == 1) "${exp.a} ${exp.op} ${exp.b} = ${res.first()}"
            else "${exp.a} ${exp.op} ${exp.b} = ?"
        }.toTypedArray()
    }

    private fun calcLeft(exp: Expression, base: Int): Int {
        val aa = exp.a.toInt(base)
        val bb = exp.b.toInt(base)

        return when(exp.op) {
            "+" -> aa + bb
            "-" -> aa - bb
            else -> 0
        }
    }

    private fun isValid(exp: Expression, base: Int): Boolean {
        val left = calcLeft(exp, base)
        val cc = exp.c!!.toInt(base)

        return left == cc
    }

    private fun getMinBase(nums: Set<String>): Int {
        return nums.maxOf { num -> num.maxOf { it.digitToInt() } } + 1
    }
}