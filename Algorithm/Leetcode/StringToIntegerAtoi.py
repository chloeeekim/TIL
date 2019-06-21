class Solution:
    def myAtoi(self, str: str) -> int:
        start = -1
        isneg = False
        res = 0
        for i, ch in enumerate(str) :
            if ch.isdigit() and start == -1 :
                start = i
            elif ch == '-' :
                isneg = True
            else :
                if start != -1 :
                    res = int(str[start, i - 1])
                else :
                    res = 0
                    break
        if isneg :
            res *= -1
        if res < -2 ** 31 :
            return -2 ** 31
        elif res > 2 ** 31 - 1 :
            return 2 ** 31 - 1
        else :
            return res