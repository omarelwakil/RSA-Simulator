import numpy as np
import random


def is_prime(p: int):
    for i in range(2, p):
        if p % i == 0:
            return False
    return True


def is_integer(s: str):
    try:
        int(s)
        return True
    except ValueError:
        return False


def gcd(a: int, b: int):
    while b != 0:
        a, b = b, a % b
    return a


def modular_inverse(a: int, m: int):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None


def key_generation(p: int, q: int):
    if p == q and is_prime(p) and is_prime(q):
        raise ValueError('ERROR(101): p and q should not be equal.')

    n = p * q
    phi = (p - 1) * (q - 1)
    print("phi: ", phi)

    selected_e = 0
    e_s = []
    for is_e in range(2, phi):
        if gcd(is_e, phi) == 1:
            e_s.append(is_e)

    if len(e_s) == 0:
        raise ValueError('ERROR(103): No e value found.')

    random_index = random.randint(0, len(e_s) - 1)
    selected_e = e_s[random_index]

    d = modular_inverse(selected_e, phi)

    return selected_e, d, n, e_s


def encryption(plaintext: str, e: int, n: int):
    plaintext_keys = [ord(p) for p in str(plaintext)]
    if (np.asarray(plaintext_keys) >= n).any():
        print(np.asarray(plaintext_keys))
        print(n)
        raise ValueError(
            'ERROR(102): Plaintext is too large. It should be less than n.')

    print("Plaintext: ", plaintext_keys)

    ciphertext_keys = np.asarray([[pow(p, e, n), chr(pow(p, e, n))]
                                  for p in plaintext_keys])
    # print("Ciphertext: ", ciphertext_keys[:, 0])

    return ','.join(np.asarray(ciphertext_keys[:, 0]).astype(str)), ''.join(np.asarray(ciphertext_keys[:, 1]).astype(str))


def decryption(ciphertext: str, d: int, n: int):
    ciphertext_keys = [int(c) for c in ciphertext.split(',')]
    print("Ciphertext: ", ciphertext_keys)

    plaintext = ''.join([chr(pow(c, d, n)) for c in ciphertext_keys])
    # print("Plaintext: ", plaintext)
    print("Plaintext: ", [pow(c, d, n) for c in ciphertext_keys])
    return plaintext


# e, d, n, _ = key_generation(73, 151)
# print("e: ", e, ", d: ", d, ", n: ", n)
# # print("possible_e: ", _)
# plaintext = "hello world"
# print("Plaintext(before): ", plaintext)
# ciphertext, _ = encryption(plaintext, e, n)
# print("Cipertext: ", ciphertext)
# plaintext = decryption(ciphertext, d, n)
# print("Plaintext(after): ", plaintext)
