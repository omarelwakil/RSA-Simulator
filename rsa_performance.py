from turtle import color
from more_itertools import last
import rsa_algorithm as rsa
import matplotlib.pyplot as plt
import random
import time


def brute_force(ciphertext: str, __plaintext: str, n: int):
    for i in range(1, n):
        if rsa.decryption(ciphertext, i, n) == __plaintext:
            return i


def chosen_ciphertext_attack(ciphertext: str, __plaintext: str, e: int, d: int, n: int):
    random_character = random.randint(0, len(rsa.CHARACTERS) - 1)
    while rsa.gcd(n, random_character) != 1:
        random_character = random.randint(0, len(rsa.CHARACTERS) - 1)

    broken_ciphertext = [rsa.mod_exponentiation(
        int(c) * pow(random_character, e), 1, n) for c in ciphertext.split(',')]

    broken_plaintext = []
    for bc in broken_ciphertext:
        broken_plaintext.append(rsa.mod_exponentiation(bc, d, n))

    plaintext = []
    for bp in broken_plaintext:
        plaintext.append(rsa.CHARACTERS[rsa.mod_exponentiation(rsa.mod_exponentiation(
            bp, 1, n) * rsa.modular_inverse(random_character, n), 1, n)])

    print("Plaintext: ", ''.join(plaintext))
    print("__plaintext: ", __plaintext)


def best_fit(X, Y):

    xbar = sum(X)/len(X)
    ybar = sum(Y)/len(Y)
    n = len(X)  # or len(Y)

    numer = sum([xi*yi for xi, yi in zip(X, Y)]) - n * xbar * ybar
    denum = sum([xi**2 for xi in X]) - n * xbar**2

    b = numer / denum
    a = ybar - b * xbar

    print('best fit line:\ny = {:.2f} + {:.2f}x'.format(a, b))

    return a, b

'''
Brute Force Attack Example for multiple private key value
'''

plaintext = 'M'
e, d, n, _ = rsa.key_generation(73, 151)
print("e: ", e, ", d: ", d, ", n: ", n)
print("Plaintext(before): ", plaintext)
ciphertext, _ = rsa.encryption(plaintext, e, n)
print("Cipertext: ", ciphertext)
print("Cipertext: ", _)
bf_d = brute_force(ciphertext, plaintext, n)
print("brute force d: ", bf_d)

'''
Chosen ciphertext attack
'''

plaintext = 'M'
e, d, n, _ = rsa.key_generation(73, 151)
print("e: ", e, ", d: ", d, ", n: ", n)
ciphertext, _ = rsa.encryption(plaintext, e, n)
chosen_ciphertext_attack(ciphertext, plaintext, e, d, n)