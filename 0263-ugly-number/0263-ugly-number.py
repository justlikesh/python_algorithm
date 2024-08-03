class Solution:
    def isUgly(self, n: int) -> bool:

        if n < 1: return False
        if n == 1: return True

        good = set([2, 3, 5])

        def ugly(a, base):
            if a in good:
                return True
            if a % base != 0:
                return False
            new_a = a // base
            return ugly(new_a, 2) or ugly(new_a, 3) or ugly(new_a, 5)

        return ugly(n, 2) or ugly(n, 3) or ugly(n, 5)

            
        