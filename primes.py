#!/usr/bin/python

# file:///Users/ykhan/hackbright/code/mit/6-00-fall-2008/contents/assignments/pset1a.pdf

"""Write a program that computes and prints the 1000th prime number. """

import math 

def prime1000():
    possible_primes = [2, 3, 5, 7] + range (3, 1000)
    for number in range (3, 1000):
        if number % 2 == 0 or number % 3 == 0 or number % 7 == 0 or number % 5 == 0:
            possible_primes.remove(number)
    return possible_primes[-1]


#print "the 1000th prime number is", prime1000()

"""
Write a program that computes the sum of the logarithms of all the primes from 2 to some 
number n, and print out the sum of the logs of the primes, the number n, and the ratio of these 
two quantities. Test this for different values of n. 
"""

def primeProduct(n):
    possible_primes = [2, 3, 5, 7] + range (3, n+1)
    for number in range (3, n+1):
        if number % 2 == 0 or number % 3 == 0 or number % 7 == 0 or number % 5 == 0:
            possible_primes.remove(number)
    #now have list of primes up to 1000
    print len(possible_primes),possible_primes

    result = 1
    for number in possible_primes:
        result *= math.log(number)
        print n, result, result/n



    

print primeProduct(3000)

