import time
def find_primes_in_range_1():
    start = time.time()
    a = range(2, 50000)
    lst = []
    for x in a:
        for b in range(2, x//2):
            if x % b == 0:
                break
        else:
            lst.append(x)
    print(len(lst))
    end = time.time()
    print(end - start)


def find_primes_in_range_2():
    start, end = [int(i) for i in input("Please enter a range with space: ").split()] # 2 50000
    begin = time.time()
    return print(f"{len([num for num in range(start, end+1) if all(num % i != 0 for i in range(2, int(num**0.5) + 1))])}\n Time: {time.time() - begin}")
    


def find_primes_in_range_3():
    """Find primes in a user-defined range using an optimized approach.ChatGPT"""
    start, end = [int(i) for i in input("Please enter a range with space: ").split()]  # Example: 2 50000
    begin = time.time()
    prime_count = sum(
        1 for num in range(start, end + 1) 
        if all(num % i != 0 for i in range(2, int(num**0.5) + 1))
    )
    print(f"Primes Found: {prime_count}")
    print(f"Time: {time.time() - begin:.6f} seconds")


find_primes_in_range_1()
find_primes_in_range_2()
find_primes_in_range_3()

"""
OUTPUT:

    5134
    1.7235217094421387
    Please enter a range with space: 2 50000
    5133
    Time: 0.05894160270690918
    Please enter a range with space: 2 50000
    Primes Found: 5133
    Time: 0.059362 seconds

"""