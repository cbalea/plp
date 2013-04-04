'''
Create a function that has as argument a number, named start_number. 
Using closures(defining a new function inside the first function), display the next 5 prime numbers, 
starting with start_number(argument from the enclosing scope).
'''
import math

def is_prime(number):
    is_prime = True
    for x in range(2, int(math.sqrt(number) + 1)):
            if number % x == 0: 
                is_prime = False
                break
    return is_prime
    

def print_primes_from(a):
    def get_primes(nbOfPrimes):
        number = a 
        printedPrimes = 0
        while printedPrimes < nbOfPrimes:
            if is_prime(number):
                printedPrimes += 1
                print number      
            number += 1
    return get_primes

b = print_primes_from(3)
b(5)