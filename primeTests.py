import timeit
import matplotlib.pyplot as plt

from primechecks.naive import nthPrime as naiventhPrime
from primechecks.trialdiv import nthPrime as trialdivnthPrime
from primechecks.eratosthenes import nthPrime as eratosthenesnthPrime
# Tests various kinds of prime numbers and records their times


def packageFunctions():
    return [
        {
            "name": "Naive",
            "nthPrime": naiventhPrime
        },
        {
            "name": "Trial Division",
            "nthPrime": trialdivnthPrime
        },
        {
            "name": "Sieve of Eratosthenes",
            "nthPrime": eratosthenesnthPrime
        }
    ]


def testFunc(nthPrime):
    for i in range(1, 100):
        nthPrime(i)


def verifyFuncs(primeFuncs):
    for primeFunc in primeFuncs:
        name = primeFunc["name"]
        nthPrime = primeFunc["nthPrime"]

        # Generate a list of primes
        primes = [nthPrime(i) for i in range(1, 10)]

        assert(primes == [2, 3, 5, 7, 11, 13, 17, 19, 23]
               ), f"[{name}] Primes are not correct: {primes}"

    print("All functions verified correct (for 10 primes).")


def main():
    primeFuncs = packageFunctions()

    verifyFuncs(primeFuncs)

    for primeFunc in primeFuncs:
        name = primeFunc["name"]
        nthPrime = primeFunc["nthPrime"]
        print(f"Testing {name}...")

        primeFunc["time"] = timeit.timeit(
            lambda: testFunc(nthPrime), number=1_000)

    # Export times to CSV
    with open("primeTests.csv", "w") as f:
        f.write("name,time\n")
        for primeFunc in primeFuncs:
            f.write(f"{primeFunc['name']},{primeFunc['time']}\n")

    # Create a bar graph of the times with matplotlib
    names = [primeFunc["name"] for primeFunc in primeFuncs]
    times = [primeFunc["time"] for primeFunc in primeFuncs]

    plt.bar(names, times)
    plt.title("Prime Number Check Times")
    plt.xlabel("Algorithm")
    plt.ylabel("Time (s)")

    # Add the times to the bars with 3 decimal places
    for i in range(len(names)):
        plt.text(names[i], times[i], f"{times[i]:.3f}")

    plt.savefig("primeTests.png")


if __name__ == "__main__":
    main()
