class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 1:
            return 0
        
        primes = [True] * n
        primes[0] = primes[1] = False
        cnt = 1

        for i in range(2, int(n**0.5) + 1):
            if primes[i]:
                for j in range(i*i, n, i):
                    if primes[j]:
                        cnt += 1
                    primes[j] = False

        return n - cnt - 1