import Encrypt
import Decrypt

##
##  Main
##

p = 101  # First random primmer
q = 103  # Second random primmer

N = p * q  # Product of p and q, modules for encryption and decryption key

encryptKey = 0  # Encryption key
decryption = 0  # Decryption key

pq = (p - 1) * (q - 1)

coprimeNumbersN = list(range(2, N))  # Coprime numbers with the chosen N
coPrimeNumbersPQ = list(range(2, pq))  # Coprime numbers with the chosen p and q

coPrimeNumbersN = Encrypt.phi(N, coprimeNumbersN, p, q)
coPrimeNumbersPQ = Encrypt.phi(pq, coPrimeNumbersPQ, p, q)

encryptKey = Encrypt.chooseencryptionkey(encryptKey, coPrimeNumbersPQ)
encryptLock = [encryptKey, N]

decryption = Decrypt.choosedecryptionkey(decryption, encryptKey, pq)
decryptionKey = [decryption, N]

print(encryptLock)
print(decryptionKey)

cryptedmessage = Encrypt.encryptmessage(22222, encryptKey, N)
decrpt = Decrypt.decryptmessage(cryptedmessage, decryption, N)

print("Ciphered message: 2, deciphered message: ")
print(decrpt)

