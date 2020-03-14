#!/usr/bin/env python

""" Problem 6
The sum of the squares of the first ten natural numbers is,

1^2+2^2+...+10^2=385
The square of the sum of the first ten natural numbers is,

(1+2+...+10)^2=55^2=3025
Hence the difference between the sum of the squares of the first ten natural numbers
and the square of the sum is 3025−385=2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

Answer: 25164150

"""


def main():
    sum_squares = calc_squares()
    square_of_sum = calc_square_of_sum()
    answer = abs(square_of_sum - sum_squares)
    return answer


def calc_squares():
    sum_of_squares = 0
    for i in range(1, 101):
        sum_of_squares += (i ** 2)
    return sum_of_squares


def calc_square_of_sum():
    square_of_sum = 0
    for i in range(1, 101):
        square_of_sum += i
    return square_of_sum ** 2


if __name__ == "__main__":
    main()
