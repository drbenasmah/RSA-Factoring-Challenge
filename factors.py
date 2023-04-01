import sys
import time

def factorize(n):
    """
    Factorize a number n into two smaller numbers.
    """
    for i in range(2, n):
        if n % i == 0:
            return i, n // i
    return None

def factorize_file(filename):
    """
    Factorize a list of numbers from a file and print the factorization for each number.
    """
    with open(filename, 'r') as f:
        numbers = [int(line.strip()) for line in f.readlines()]

    for n in numbers:
        start_time = time.monotonic()
        factors = factorize(n)
        elapsed_time = time.monotonic() - start_time

        if factors is None:
            print(f"Could not factorize {n}")
        else:
            print(f"{n}={factors[0]}*{factors[1]} (elapsed time: {elapsed_time:.6f}s)")

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python factors.py <file>")
        exit(1)

    filename = sys.argv[1]
    factorize_file(filename)