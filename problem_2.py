#! /usr/bin/env python


""" https://projecteuler.net/problem=2
Each new term in the Fibonacci sequence is generated by adding the previous two terms.
By starting with 1 and 2, the first 10 terms will be:
1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
By considering the terms in the Fibonacci sequence whose values do not exceed four million,
find the sum of the even-valued terms.
Answer: 4613732
"""


def main():
    # print(fibonacci_sequence(5)) # test
    # print(fibonacci_sequence(10)) # test
    return fibonacci_sequence(4_000_000)


def fibonacci_sequence(n):
    """implement problem 2"""
    a = 0
    b = 1
    total = 0
    if a < 0:
        print("input smaller than zero")
    elif n == 0:
        return a
    elif n == 1:
        return b
    else:
        while total < n:
            c = a + b
            a = b
            b = c
            if b % 2 == 0:
                total += b
            # print(b)
    return total


if __name__ == "__main__":
    main()
