#!/usr/bin/env python


"""

A palindromic number reads the same both ways.

The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.

Answer: 906609
"""


def main():
    largest_palindrome = 0
    for i in range(999):
        for j in range(999, 100, -1):
            number = i * j
            if str(number) == str(number)[::-1]: # if palindrome
                if largest_palindrome < int(number):
                    largest_palindrome = int(number)
    return largest_palindrome


if __name__ == "__main__":
    main()


