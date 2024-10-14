class Solution:
    def integerBreak(self, n: int) -> int:
        if n < 4:
            return n-1
        prod = 1
        while n > 4:
            prod *= 3
            n-=3
        return prod * n