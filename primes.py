"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    if not (number_of_primes > 0):
        raise ValueError(f'The number of primes, {number_of_primes}, should be a positive number.')

    list = []

    currentNum = 2

    while len(list) < number_of_primes:
        #check if the current number is a multiple of any prime we already have
        multipleOfNum = False
        for p in list:
            if (currentNum % p) == 0 :
                multipleOfNum = True
                break
        #Not a multiple of a number // hence prime
        if not multipleOfNum:
            list.append(currentNum)

        #Increment current number
        currentNum += 1

    return list
