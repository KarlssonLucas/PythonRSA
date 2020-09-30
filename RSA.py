#
#   Python RSA Encryption and decryption, made for personal use and to learn how and why people use it
#
import random
import math

p = 23  # First random primmer
q = 31  # Second random primmer

N = p * q  # Product of p and q, modules for encryption and decryption key

encryptKey = 0  # Encryption key
decryption = 0  # Decryption key

pq = (p - 1) * (q - 1)

coprimeNumbersN = list(range(2, N))  # Coprime numbers with the chosen N
coPrimeNumbersPQ = list(range(2, pq))  # Coprime numbers with the chosen p and q


def phi(n, coPrimeNumbers):
    for i in range(2, n):
        if any([i % 2 == 0, n % i == 0, i % p == 0, i % q == 0, not is_prime(i)]):
            coPrimeNumbers.remove(i)


def chooseencryptionkey(e):
    ran = random.randrange(1, len(coPrimeNumbersPQ))
    e = coPrimeNumbersPQ[ran]
    return e


def choosedecryptionkey(d, e, n):
    for i in range(1, 999):
        if (i * e) % n == 1:
            d = i
            break
    return d


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


#############################################################


def encryptmessage(message, en):
    re = message ** en % N

    return re


def decryptmessage(encryption, dec):
    en = encryption ** dec % N
    return en


phi(N, coprimeNumbersN)
phi(pq, coPrimeNumbersPQ)

encryptKey = chooseencryptionkey(encryptKey)
encryptLock = [encryptKey, N]

decryption = choosedecryptionkey(decryption, encryptKey, pq)
decryptionKey = [decryption, N]

print(encryptLock)
print(decryptionKey)

cryptedmessage = encryptmessage(2, encryptKey)
decrpt = decryptmessage(cryptedmessage, decryption)

print("Ciphered message: 2, deciphered message: ")
print(decrpt)
