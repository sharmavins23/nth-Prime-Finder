import math
# Compute primes via the Sieve of Eratosthenes


def nthPrime(n):
    # Compute the upper bound
    if n >= 6:
        upperBound = math.ceil(n * (math.log(n) + math.log(math.log(n))))
    else:
        upperBound = 13

    # Create a list of all numbers up to the upper bound
    numbers = list(primesUpTo(upperBound))

    return numbers[n-1]


# From https://stackoverflow.com/a/33014445
def primesUpTo(limit):
    prime = [True] * limit

    for n in range(2, limit):
        if prime[n]:
            yield n  # n is a prime

            for c in range(n*n, limit, n):
                prime[c] = False  # Mark composites
