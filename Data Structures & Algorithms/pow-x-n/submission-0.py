
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        exp_sign = 1 if n > 0 else -1
        n = abs(n)
        pows = {1: x if exp_sign == 1 else 1/x} # pow[i] = x^i or x^-i if n < 0

        exponents = [1]
        i = 2
        while i <= n:
            pows[i] = pows[i / 2] * pows[i / 2]
            exponents.append(i)
            i *= 2
        
        # multiply the powers to get result
        res = 1
        i = len(exponents) - 1
        while n >= 1:
            print(f'{res=} {i=} {n=}')
            exp = exponents[i]
            if exp > n:   # cant multiply by ths exponent as its too big
                i -= 1
                continue
            res *= pows[exp]  # multiply res by maximum possible exponent
            n -= exp  # the exponent left needed decreases
            i -= 1
        
        return res

            

