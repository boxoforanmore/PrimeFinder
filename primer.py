import unittest
import csv


class PrimeNumbers():
    def __init__(self, lower = 2, upper = 10, filename = 'primesList.log'):
        self.__filename = filename
        self.__primes = []
        self.upper = upper
        self.lower = lower

        ## Fix error messages
        if self.upper <= 1:
            raise RuntimeError("The upper limit must be greater than 1; %d is not a prime number (between 2 and inf)", self.lower)

        if self.lower <= 1:
            raise RuntimeError("The lower limit must be greater than 1; %d is not a prime number (between 2 and inf)", self.lower)
         
        if self.lower >= self.upper:
            raise RuntimeError("The upper limit must be greater than the lower limit; %d is not greater than %d", self.upper, self.lower)

  
        #for i in range(self.lower, self.upper):
        #    if self.__is_prime(i):
        #        self.__primes.append(i)

    ## Read and input CSV to skip redoing previous numbers
    ## Have the prime generator stop at the 50% mark so that O(n/2)

    ## add a break for if prime is more than halfway through the list
    def __is_prime(self, num):
        for prime in self.__primes:
            if((num % prime) == 0):
                return False
        return True

    def __from_file(self):
        with open(self.__filename, "r") as inputNumbers:
            for item in inputNumbers:
                pass

    def add_primes(self):
        self.__from_file()
        if self.lower > 2 and self.__primes == []:
            for i in range(2, self.lower):
                if self.__is_prime(i):
                    self.__primes.append(i)
        if len(self.__primes) > 0:
            self.lower = self.__primes[len(self.__primes) - 1] + 1
        for num in range(self.lower, self.upper):
            if self.__is_prime(num):
                self.__primes.append(num)

    def print_primes_into_filei(self):

        for prime in self.__primes:
            pass
            #print("%d," prime)


    def __str__(self):
        temp = []
        for i in self.__primes:
            if (i >= self.lower) and (i <= self.upper):
                temp.append(i)
        return str(temp)


class Test_Primes(unittest.TestCase):
    def test_zero_upper(self):
        self.assertRaises(RuntimeError, lambda: PrimeNumbers(upper=0))

    def test_zero_lower(self):
        self.assertRaises(RuntimeError, lambda: PrimeNumbers(lower=0))

    def test_upper_smaller_lower(self):
        self.assertRaises(RuntimeError, lambda: PrimeNumbers(lower=10, upper=3))

    def test_default(self):
        primes = PrimeNumbers()
        primes.add_primes()
        self.assertEqual("[2, 3, 5, 7]", str(primes))

    def test_larger_upper(self):
        primes = PrimeNumbers(upper=30)
        primes.add_primes()
        self.assertEqual("[2, 3, 5, 7, 11, 13, 17, 19, 23, 29]", str(primes))

    def test_moved_range(self):
        primes = PrimeNumbers(lower=20, upper=50)
        primes.add_primes()
        self.assertEqual("[23, 29, 31, 37, 41, 43, 47]", str(primes))



if '__main__' == __name__:
    unittest.main()
