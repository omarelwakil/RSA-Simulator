import numpy as np
import random


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def modular_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None


def key_generation(p, q):
    if p == q:
        raise ValueError('ERROR(101): p and q should not be equal.')

    n = p * q
    phi = (p - 1) * (q - 1)

    selected_e = 0
    e_s = []
    for is_e in range(2, phi):
        if gcd(is_e, phi) == 1:
            e_s.append(is_e)

    random_index = random.randint(0, len(e_s) - 1)
    selected_e = e_s[random_index]

    d = modular_inverse(selected_e, phi)

    return selected_e, d, n, e_s


def encryption(plaintext, e, n):
    plaintext_keys = [ord(p) for p in str(plaintext)]

    if (np.asarray(plaintext_keys) >= n).any():
        raise ValueError(
            'ERROR(102): Plaintext is too large. It should be less than n.')

    # print("Plaintext: ", plaintext_keys)

    ciphertext_keys = [pow(p, e, n) for p in plaintext_keys]
    # print("Ciphertext: ", ciphertext_keys)

    return ','.join(np.asarray(ciphertext_keys).astype(str))


def decryption(ciphertext, d, n):
    ciphertext_keys = [int(c) for c in ciphertext.split(',')]
    # print("Ciphertext: ", ciphertext_keys)

    plaintext = ''.join([chr(pow(c, d, n)) for c in ciphertext_keys])
    # print("Plaintext: ", plaintext)

    return plaintext


e, d, n, _ = key_generation(73, 17)
print("e: ", e, ", d: ", d, ", n: ", n)
# print("possible_e: ", _)
plaintext = "hello world"
print("Plaintext(before): ", plaintext)
ciphertext = encryption(plaintext, e, n)
print("Cipertext: ", ciphertext.replace(',', ''))
plaintext = decryption(ciphertext, d, n)
print("Plaintext(after): ", plaintext)

