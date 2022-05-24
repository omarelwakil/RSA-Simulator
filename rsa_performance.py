from turtle import color
from more_itertools import last
import rsa_algorithm as rsa
import matplotlib.pyplot as plt
import random
import time


def brute_force(ciphertext: str, __plaintext: str, n: int):
    # arr = []
    for i in range(1, n):
        if rsa.decryption(ciphertext, i, n) == __plaintext:
            # print("Decryption successful:", rsa.decryption(ciphertext, i, n))
            # print("Decryption successful:", __plaintext)
            # print("d value: ", i)
            # arr.append(i)
            # print(rsa.decryption(ciphertext, i, n) == __plaintext)
            return True


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
BRUTE FORCE ATTACK
'''

# prime_numbers = [7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107,
#                  109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239]
# primes_dict = dict(zip(prime_numbers, [i for i in range(len(prime_numbers))]))

# encryption_times = []
# break_rsa = []

# plaintext = "hello world"
# plaintext_2 = "012"
# key_lengths = [(5, 3), (7, 3), (11, 3),
#                (13, 3), (13, 5), (13, 7), (13, 11)]
# last_p = 13
# last_q = 11
# checker = False
# for q in range(1, 2000):
#     if primes_dict[last_p] == len(prime_numbers) - 1 or primes_dict[last_q] == len(prime_numbers) - 1:
#         break
#     if checker:
#         last_p = prime_numbers[primes_dict[last_p] + 1]
#         checker = False
#     else:
#         last_q = prime_numbers[primes_dict[last_q] + 1]
#         checker = True

#     if last_p == last_q:
#         continue
#     key_lengths.append((last_p, last_q))

# print(key_lengths)

# for p, q in key_lengths:
#     e, d, n, _ = rsa.key_generation(p, q)
#     print(n)
#     start = time.time()
#     if n > 62:
#         ciphertext, _ = rsa.encryption(plaintext, e, n)
#     else:
#         ciphertext, _ = rsa.encryption(plaintext_2, e, n)
#     end = time.time()
#     encryption_times.append((n, (end - start) * 1000))

#     start = time.time()
#     if n > 62:
#         brute_force(ciphertext, plaintext, n)
#     else:
#         brute_force(ciphertext, plaintext_2, n)
#     end = time.time()
#     break_rsa.append((n, (end - start) * 1000))

# print("------------------------------------")
# print(encryption_times)
# print("------------------------------------")
# print(break_rsa)

# a, b = best_fit([i[1] for i in encryption_times], [i[0]
#                 for i in encryption_times])
# plt.scatter([i[1] for i in encryption_times], [i[0]
#                                                for i in encryption_times], label="Encryption Time vs n")
# plt.xlabel("Encryption Time (s)")
# plt.ylabel("n")
# yfit = [a + b * xi for xi in [i[1] for i in encryption_times]]
# plt.plot([i[1] for i in encryption_times], yfit, color='red')
# plt.show()

# a, b = best_fit([i[1] for i in break_rsa], [i[0] for i in break_rsa])
# plt.scatter([i[1] for i in break_rsa], [i[0]
#                                         for i in break_rsa], label="Brute force vs n")
# plt.xlabel("Broken Time (s)")
# plt.ylabel("n")
# yfit = [a + b * xi for xi in [i[1] for i in break_rsa]]
# plt.plot([i[1] for i in break_rsa], yfit, color='red')
# plt.show()

# --------------------------------------------------------------------------
# --------------------------------------------------------------------------
# --------------------------------------------------------------------------
# --------------------------------------------------------------------------
# --------------------------------------------------------------------------
'''
Chosen ciphertext attack
'''

# e, d, n, _ = rsa.key_generation(59, 53)
# print("e:", e)
# print("d:", d)
# print("n:", n)
# plaintext = "hello world"
# ciphertext, _ = rsa.encryption(plaintext, e, n)
# chosen_ciphertext_attack(ciphertext, plaintext, e, d, n)
