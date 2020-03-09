#! /usr/bin/env python


""" https://projecteuler.net/problem=1
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
The sum of these multiples is 23. Find the sum of all the multiples of 3 or 5 below 1000.
Answer: 233168
"""


def main():
    numbers = compose_list(1000)
    return adding(numbers)


def compose_list(n):
    """first adding the numbers that are multiples of 3 and 5"""
    list = []
    for i in range(0, n):
        if (i % 3 == 0) or (i % 5 == 0):
            list.append(i)
    return list


def adding(array):
    """then simply add all the numbers"""
    answer = 0
    for i in array:
        answer += i
    return answer


if __name__ == "__main__":
    main()
