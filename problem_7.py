#!/usr/bin/env python

""" Problem 7
10001st prime

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10,001st prime number?

Answer = 104743
"""


def main():
    upper_limit = 10001
    counter = 1
    prime_list = []
    prime_list.append(2)

    while len(prime_list) < upper_limit:
        counter += 2
        j = 0
        is_prime = True
        while prime_list[j] * prime_list[j] <= counter:
            if counter % prime_list[j] == 0:
                is_prime = False
                break
            j += 1
        if is_prime:
            prime_list.append(counter)
    return prime_list[upper_limit-1]


if __name__ == "__main__":
    main()
