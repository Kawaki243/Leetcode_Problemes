class Solution:
	# quick pow
    def myPow(self, x: float, n: int) -> float:
        res = 1
        sign = n>=0
        n = abs(n)
        while n:
            # bit-wise AND -> + operator in base2, test if the least bit of 'n' is one
            if n&1:
                res *= x

            # bit-shift n  (equivalent to n//2) remove least bit of n
            n = n>>1
            x *= x
            print(x)
        return res if sign else 1/res