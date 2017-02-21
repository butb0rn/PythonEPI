import unittest

def generatePrimes(n):
    if n < 2: return []
    primes = []
    isPrime = [True for i in range(n+1)]
    isPrime[0], isPrime[1] = False, False #0,1

    for p in range(2, n+1):
        if isPrime[p]:
            primes.append(p)
            for j in range(p, n+1, p):
                isPrime[j] = False

    return primes


class TestGeneratePrimes(unittest.TestCase):
    def test_primes_not_exist_for_one(self):
        self.assertEqual(generatePrimes(1), [])

    def test_primes_not_exist_for_zero(self):
        self.assertEqual(generatePrimes(0), [])

    def test_primes_not_exist_for_18(self):
        self.assertEqual(generatePrimes(18), [2, 3, 5, 7, 11, 13, 17])










if __name__ == "__main__": unittest.main()
