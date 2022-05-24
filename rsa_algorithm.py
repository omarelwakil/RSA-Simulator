import numpy as np
import random

CHARACTERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
              'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', ' ']
INDICES = [CHARACTERS.index(i) for i in CHARACTERS]
CHARACTERS_DICT = dict(zip(CHARACTERS, INDICES))


def mod_exponentiation(a: int, b: int, m: int):
    result = 1
    while b > 0:
        if b % 2 == 1:
            result = (result * a) % m
        a = (a * a) % m
        b = b // 2
    return result


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
    return 0


def key_generation(p: int, q: int):
    if p == q or not is_prime(p) or not is_prime(q):
        raise ValueError(
            'ERROR(101): {} and {} should not be equal and both should be prime.'.format(p, q))

    n = p * q
    phi = (p - 1) * (q - 1)
    # print("phi: ", phi)

    selected_e = 0
    e_s = []
    for is_e in range(2, phi):
        if gcd(phi, is_e) == 1 and is_e > 1 and is_e < phi:
            e_s.append(is_e)

    if len(e_s) == 0:
        raise ValueError('ERROR(102): No e value found.')

    random_index = random.randint(0, len(e_s) - 1)
    selected_e = e_s[random_index]
    selected_e = 3

    d = modular_inverse(selected_e, phi)

    return selected_e, d, n, e_s


def encryption(plaintext: str, e: int, n: int):
    plaintext_keys = None
    try:
        plaintext_keys = [CHARACTERS_DICT[p] for p in str(plaintext)]
    except:
        raise ValueError(
            'ERROR(103): Plaintext is not valid. Plaintext contains characters not alphanumeric nor space.')
    # print(plaintext)
    if (np.asarray(plaintext_keys) >= n).any():
        raise ValueError(
            'ERROR(104): Plaintext is too large. It should be less than n.')

    # print("Plaintext: ", plaintext_keys)

    ciphertext_keys = []
    for p in plaintext_keys:
        c = mod_exponentiation(p, e, n)
        ciphertext_keys.append([c, chr(c)])
    ciphertext_keys = np.asarray(ciphertext_keys)

    # print("Ciphertext: ", ciphertext_keys[:, 0])

    return ','.join(np.asarray(ciphertext_keys[:, 0]).astype(str)), ''.join(np.asarray(ciphertext_keys[:, 1]).astype(str))


def decryption(ciphertext: str, d: int, n: int):
    ciphertext_keys = [int(c) for c in ciphertext.split(',')]
    # print("Ciphertext: ", ciphertext_keys)

    # plaintext = ''.join([CHARACTERS[mod_exponentiation(c, d, n)]
    #                     for c in ciphertext_keys])
    plaintext = []
    for c in ciphertext_keys:
        index = mod_exponentiation(c, d, n)
        if index < len(CHARACTERS):
            plaintext.append(CHARACTERS[index])
        else:
            plaintext.append('*')

    # print("Plaintext: ", ''.join(plaintext))
    return ''.join(plaintext)


# e, d, n, _ = key_generation(73, 151)
# print("e: ", e, ", d: ", d, ", n: ", n)
# print("possible_e: ", _)
# plaintext = "hello world"
# print("Plaintext(before): ", plaintext)
# ciphertext, _ = encryption(plaintext, e, n)
# print("Cipertext: ", ciphertext)
# plaintext = decryption(ciphertext, d, n)
# print("Plaintext(after): ", plaintext)
