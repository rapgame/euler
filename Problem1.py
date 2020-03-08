#!/usr/bin/python

# https://projecteuler.net/problem=1
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
# The sum of these multiples is 23. Find the sum of all the multiples of 3 or 5 below 1000.
# Answer: 266333


def main():
    numbers = composer()
    print(adding(numbers))


def composer():
    list = []
    for i in range(1000):
        if i % 3 == 0:
            list.append(i)
        if i % 5 == 0:
            list.append(i)
    return list


def adding(array):
    answer = 0
    for i in array:
        answer += i
    return answer


if __name__ == "__main__":
    main()
