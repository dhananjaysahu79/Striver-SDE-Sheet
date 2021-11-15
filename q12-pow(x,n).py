# Fast | Binary Exponentiation
# O(longN) Solution

class Solution:
    def myPow(self, x: float, n: int) -> float:

        def fastPow(x,n):
            if n == 0: return 1
            if n < 0: return fastPow(1/x, -n)
            if n & 1: return x * fastPow(x*x, n//2)
            return fastPow(x*x, n//2)
        return fastPow(x,n)