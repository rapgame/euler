# /usr/bin/env python

""" Problem 5

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

Answer: 2584
"""

import math

def main():
    i = 20
    while (i % 2 != 0 or i % 3 != 0 or i % 4 != 0 or i % 5 != 0 or i % 6 != 0 or
           i % 7 != 0 or i % 8 != 0 or i % 9 != 0 or i % 10 != 0 or i % 11 != 0 or
           i % 12 != 0 or i % 13 != 0 or i % 14 != 0 or i % 15 != 0 or i % 16 != 0 or
           i % 17 != 0 or i % 18 != 0 or i % 19 != 0 or i % 20 != 0):
        i += 20
    return i

# def second_solution():
#     divisor_max = 20;
#     p = math.p(divisor_max);
#     int
#     result = 1;
#
#     for (int i = 0; i < p.Length; i++) {
#         int a = (int) math.Floor(Math.Log(divisorMax) / math.Log(p[i]));
#     result = result * ((int)Math.Pow(p[i], a));
#     }


if __name__ == "__main__":
    main()
