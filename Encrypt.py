##
##  Encryption
##

import random


def phi(n, coPrimeNumbers, p, q):
    for i in range(2, n):
        if any([i % 2 == 0, n % i == 0, i % p == 0, i % q == 0, not is_prime(i)]):
            coPrimeNumbers.remove(i)

    return coPrimeNumbers


def chooseencryptionkey(e, coPrimeNumbersPQ):
    ran = random.randrange(1, len(coPrimeNumbersPQ))
    e = coPrimeNumbersPQ[ran]
    print(e)
    return e


def is_prime(n):
    if n == 2 or n == 3: return True
    if n < 2 or n % 2 == 0: return False
    if n < 9: return True
    if n % 3 == 0: return False
    r = int(n ** 0.5)

    # since all primes > 3 are of the form 6n ± 1
    # start with f=5 (which is prime)
    # and test f, f+2 for being prime
    # then loop by 6.

    f = 5
    while f <= r:
        if n % f == 0: return False
        if n % (f + 2) == 0: return False
        f += 6
    return True


def encryptmessage(message, en, n):
    re = message ** en % n

    return re
