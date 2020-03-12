#!/usr/bin/env python

"""
Largest prime factor

Problem 3
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

"""


class Problem3:
    """
    The problem 3 implementation
    What is the largest prime factor of the number 600851475143 ?
    answer: 6857
    """


    @staticmethod
    def get_largest_prime_factor():
        """
        https://www.mathsisfun.com/prime-factorization.html
        :param number: the given input for this problem
        :return: the largest prime factor of the given number
        """
        number = 600851475143
        new_number = number
        largest_factor = 0
        counter = 2

        while counter * counter <= new_number:
            if new_number % counter == 0: # a prim is
                new_number = new_number / counter
                largest_factor = counter
            else:
                counter += 1

        if new_number > largest_factor:
            largest_factor = new_number

        return largest_factor

