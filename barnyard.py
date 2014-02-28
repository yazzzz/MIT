#!/usr/bin/python

"""
The problem is as follows: Given the number of heads and feet counted on a farm, 
compute the number of pigs and chickens, assuming that each pig has one head and four feet 
and that each chickens has one head and two feet.

YAZ NOTE: i approached this problem as "given the number of heads and number of feet, find how
many pigs or chickens you could have inside those limits"

"""

bruteForce(4, 10)

def howManyPigs(heads, feet):
    """here we use the max number of pigs"""
    chicken_feet = 2
    pig_feet = 4
    num_chickens = 0
    num_pigs = 0

    num_pigs = min(feet/pig_feet,heads)
    print "initial number of pigs is", num_pigs, ",that uses up", (num_pigs*4), "feet"
    remaining_feet = feet % (num_pigs*4)
    print "so we have", remaining_feet ,"feet left over...let's add to the chickens"


    num_chickens += remaining_feet/2
    print "\ntotal chickens:", num_chickens 
    print "total pigs", num_pigs


#howManyPigs(13, 35)  # answer 9, 4


def howManyChickens(heads, feet):
    """here we use the max number of chickens"""
    chicken_feet = 2
    pig_feet = 4
    num_chickens = 0
    num_pigs = 0

    num_chickens = min(feet/chicken_feet,heads)
    print "initial number of chickens is", num_chickens, ",that uses up", (num_chickens*2), "feet"
    remaining_feet = feet % (num_chickens*2)
    print "so we have", remaining_feet ,"feet left over...let's add to the pigs"

    num_chickens -= remaining_feet/2
    num_pigs += remaining_feet/2
    print "\ntotal chickens:", num_chickens 
    print "total pigs", num_pigs


howManyChickens(13, 35)  # answer 9, 4

# brute force

def solve(numLegs, numHeads): 
    for numChicks in range(0, numHeads + 1):
        numPigs = numHeads - numChicks
        totLegs= 4*numPigs + 2*numChicks 
        if totLegs == numLegs:
            return (numPigs, numChicks) 
    return (None, None)

def barnYard(): 
    heads = 13    
    legs = 35
    pigs, chickens = solve(legs, heads) 
    if pigs == None: 
        print 'There is no solution' 
    else: 
        print 'Number of pigs:', pigs
    print 'Number of chickens:', chickens


barnYard()