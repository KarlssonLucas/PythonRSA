##
## Decryption
##


def choosedecryptionkey(d, e, n):
    for i in range(1, n):
        if (i * e) % n == 1:
            d = i
            print(d)
            break
    return d


def decryptmessage(encryption, dec, n):
    en = encryption ** dec % n
    return en
