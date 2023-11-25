import time
import binary
import trivial

def compare(l: list, v: int):
    # Test the trivial algorithm
    start_time = time.time()
    trivial.trivial_search(l, v)
    end_time = time.time()
    trivial_time = end_time - start_time
    print(trivial_time)

    # Test the binary search algorithm
    start_time = time.time()
    binary.binary_search(l, v)
    end_time = time.time()
    binary_time = end_time - start_time
    print(binary_time)

# With this setup, the trivial algorithm ran in about 330 seconds on my machine, any searched value over 10^9 takes way too long
compare(range(1000000000000000000), 1000000000)