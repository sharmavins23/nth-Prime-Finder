import timeit
import matplotlib.pyplot as plt

from primechecks.naive import isPrime as naiveIsPrime
from primechecks.logcheck import isPrime as logcheckIsPrime
# Tests various kinds of prime numbers and records their times


def packageFunctions():
    return [
        {
            "name": "naive",
            "isPrime": naiveIsPrime
        },
        {
            "name": "logcheck",
            "isPrime": logcheckIsPrime
        }
    ]


def testFunc(isPrime):
    for i in range(1, 1_000):
        isPrime(i)


def main():
    primeFuncs = packageFunctions()

    for primeFunc in primeFuncs:
        name = primeFunc["name"]
        isPrime = primeFunc["isPrime"]
        print(f"Testing {name}...")

        primeFunc["time"] = timeit.timeit(
            lambda: testFunc(isPrime), number=1_000)

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
    plt.savefig("primeTests.png")


if __name__ == "__main__":
    main()
