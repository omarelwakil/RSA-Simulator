# RSA Simulator
We have simulated a sender/reciever using RSA Algorithm referenced in `Cryptography and Network Security Principles and Practice, 5th  Edition`. We have also implemented 2 types of attacks.

## Types of attacks
1. Bruteforce (BF).
2. Chosen Cipher Attack (CCA).

## Notes
1. You can read more about the project in `Security Project Spring 2022.pdf`.
2. If you tried bruteforce attack, you will find that there are multiple private key values that can decrypt the message.

### BF Attack Example for multiple private key value
```python
import rsa_algorithm as rsa
import rsa_performance as attacks

plaintext = 'M'
p = 73
q = 151
e, d, n, _ = rsa.key_generation(p, q)
# e:  41 , d:  3161 , n:  11023
ciphertext, _ = rsa.encryption(plaintext, e, n)
# ciphertext as number: 2067
# ciphertext as str: ࠓ
bf_d = attacks.brute_force(ciphertext, plaintext, n)
# private key (brute forced): 461
```
You can see that the true private key is not equal to brute forced private key.