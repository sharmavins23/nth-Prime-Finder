import math
# Naive, but with isPrime check up to roots of n


def nthPrime(n):
    primes = []
    i = 2
    while True:
        if isPrime(i):
            primes.append(i)
        if len(primes) >= n:
            break
        i += 1

    return primes[-1]


def isPrime(n):
    if n == 2:
        return True

    topBound = math.floor(math.sqrt(n))

    for i in range(2, topBound+1):
        if n % i == 0:
            return False

    return True


if __name__ == '__main__':
    # Generate a list of primes
    primes = [nthPrime(i) for i in range(1, 10)]

    assert(primes == [2, 3, 5, 7, 11, 13, 17, 19, 23]
           ), f"Primes are not correct: {primes}"
