import math
import random


# TODO Find Greatest Common Divisor using Euclid's algorithm
def gcd(a, b):
    #code goes here

    # return gcd
    return


# Find the multiplicative inverse of two numbers Euclid's extended algorithm
def multiplicative_inverse(e, t):
    d = 0
    x1 = 0
    x2 = 1
    y1 = 1
    temp_t = t

    while e > 0:
        temp1 = temp_t//e
        temp2 = temp_t - temp1 * e
        temp_t = e
        e = temp2

        x = x2 - temp1 * x1
        y = d - temp1 * y1

        x2 = x1
        x1 = x
        d = y1
        y1 = y

    if temp_t == 1:
        return d + t


# TODO: Check if number is prime or not
def prime_check(num):
    # code goes here

    return True


# Generate Public and Private Keys
def key_gen(p, q):
    #TODO
    # 1. Check if p and q are primes
    # 2. p and q can no tbe equal
    # 3. Compute value of n such that:  n= p * q
    # 4. Find the value of totient(t) such that: t = (p-1) * (q-1)
    # 5. Choose integer e such that e and t are co-prime [HINT: Use the  defined gcd() method]
    # 6. Choose value of d such that (p * q) mode n = 1
    # [HINT: find multiplicative inverse using Extended Euclid's Algorithm] [ check out the multiplicative_inverse(e, t)]]
    #  Generate and return the public and private key.

    return


# Encrypt data using Public Key
def encrypt(public_key_pair, user_message):
    #TODO: Convert each letter to ints ASCII value and Encrypt each value using formula: encryption = message ^ e mod N
    # return ciphered text array
    return


# Decrypt data using Private Key
def decrypt(private_key_pair,  cipher):
    #TODO: Decrypt the cipher using formula: decryption = encrypted_message ^ d mod N
    # Convert ASCII code to characters
    # return decrypted_text

    return


if __name__ == '__main__':

    print("!!!===== Encryption and Decryption using RSA Algorithm ========!!")
    print(" ")

    p = int(input(" Enter a prime number (greater than 10): "))
    q = int(input(" Enter another prime number (Not one you entered above and greater than 10): "))

    print(" Generating Public and Private key....")

    public, private = key_gen(p, q)
    print(" Public key: ", public)
    print(" Private key: ", private)

    message = input(" Enter a message to encrypt: ")
    encrypted_msg = encrypt(public, message)
    print(" Encrypting message using public key", public, ". . .")
    print(" Encrypted message is: ", ''.join(map(lambda x: str(x), encrypted_msg)))
    print(" Decrypting message using private key", private, " . . .")
    print(" Decrypted message is: ", decrypt(private, encrypted_msg))