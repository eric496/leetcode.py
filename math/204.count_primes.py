'''
Count the number of prime numbers less than a non-negative number, n.

Example:

Input: 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
'''

# Sieve of Eratosthenes
# read https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 3:
            return 0
        primes = [1] * n
        primes[0] = primes[1] = 0
        for i in range(2, int(n**0.5)+1):
            if primes[i] == 1:
                for j in range(i*i, n, i):
                    primes[j] = 0
        return sum(primes)