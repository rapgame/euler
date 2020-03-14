#! /usr/bin/env python


import problem_1
import problem_2
import problem_3
import problem_4
import problem_5
import problem_6
#import problem_7
#import problem_8
#import problem_9
#import problem_10


def main():
    #first_5()
    next_5()


def first_5():
    """ the famous main running all solved problems"""
    print("Problem 1: " + str(problem_1.main()))
    print("Problem 2: " + str(problem_2.main()))
    problem3 = problem_3.Problem3
    print("Problem 3: " + str(problem3.get_largest_prime_factor()))
    print("Problem 4: " + str(problem_4.main()))
    print("Problem 5: " + str(problem_5.main()))


def next_5():
    print("Problem 6: " + str(problem_6.main()))
    #print("Problem 7: " + str(problem_7.main()))
    #print("Problem 8: " + str(problem_8.main()))
    #print("Problem 9: " + str(problem_9.main()))
    #print("Problem 10: " + str(problem_10.main()))


if __name__ == "__main__":
    main()
