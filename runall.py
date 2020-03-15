#! /usr/bin/env python


import problem_1
import problem_2
import problem_3
import problem_4
import problem_5
import problem_6
import problem_7


def main():
    #first_5()
    next_2()


def first_5():
    """ the famous main running all solved problems"""
    print("Problem 1: " + str(problem_1.main()))
    print("Problem 2: " + str(problem_2.main()))
    problem3 = problem_3.Problem3
    print("Problem 3: " + str(problem3.get_largest_prime_factor()))
    print("Problem 4: " + str(problem_4.main()))
    print("Problem 5: " + str(problem_5.main()))


def next_2():
    print("Problem 6: " + str(problem_6.main()))
    print("Problem 7: " + str(problem_7.main()))


if __name__ == "__main__":
    main()
