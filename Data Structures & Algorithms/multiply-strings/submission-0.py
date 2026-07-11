class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        n = len(num1)
        m = len(num2)

        res = 0
        for i in range(n - 1, -1, -1):
            carry = 0
            exp = n - 1 - i
            for j in range(m - 1, -1, -1):
                digit_1 = int(num1[i])
                digit_2 = int(num2[j])
                carry, a = divmod(digit_1 * digit_2 + carry, 10)
                res += a * 10**exp

                exp += 1

            if carry:
                res += carry * 10 ** exp
            print(f'{i=} {j=} {exp=} {carry=} {a=} {res=}')

        return str(res)