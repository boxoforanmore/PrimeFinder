import unittest
import csv


class PrimeNumbers():
    def __init__(self, limit = 100, filename = 'primes.csv'):
        self.filename = filename
        self.primes = [1]
        self.limit = limit

        

        for i in range(2, limit):
            if self.__is_prime(i):
                self.primes.append(i)

    ## Read and input CSV to skip redoing previous numbers
    ## Have the prime generator stop at the 50% mark so that O(n/2)

    def __is_prime(self, num):
        for prime in self.primes:
            if (prime != 1) and ((num % prime) == 0):
                return False
        return True

    def print_primes_as_csv:

        for prime in self.primes:
            print("%d," prime)


primes = PrimeNumbers(100000)

