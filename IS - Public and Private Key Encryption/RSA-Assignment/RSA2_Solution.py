import math
import random


# Find Greatest Common Divisor using Euclid's algorithm
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


# Finding the multiplicative inverse of two numbers Euclid's extended algorithm
def multiplicative_inverse(e, phi):
    d = 0
    x1 = 0
    x2 = 1
    y1 = 1
    temp_phi = phi

    while e > 0:
        temp1 = temp_phi//e
        temp2 = temp_phi - temp1 * e
        temp_phi = e
        e = temp2

        x = x2 - temp1 * x1
        y = d - temp1 * y1

        x2 = x1
        x1 = x
        d = y1
        y1 = y

    if temp_phi == 1:
        return d + phi


# number is prime or not
def prime_check(num):
    if num < 2 or num % 2 == 0:
        return False
    if num == 2:
        return True
    # number must have a factor less than the square root of that number
    # skipping all the even numbers
    for n in range(3, math.floor(math.sqrt(num)), 2):
        if num % n == 0:
            return False
    return True


# Generate Public and Private Keys
def key_gen(p, q):
    if not (prime_check(p) and prime_check(q)):
        raise Exception('Both numbers must be prime')
    elif p == q:
        raise Exception('p and q cannot be equal')

    # n = pq
    n = p * q
    #print("N =", n)

    # Totient of n (t)
    t = (p-1) * (q-1)
    print(" t: ", t)

    # Choose integer e such that e and t are co-prime
    e = random.randrange(1, t)
    print(' e: ', e)

    # Check e and t are co-prime using Euclid's algorithm

    g = gcd(e, t)
    # If e and t are not co-prime change the value of e
    while g != 1:
        e = random.randrange(1, t)
        g = gcd(e, t)
    #print("G = ", g)

    # Find d using Extended Euclid's Algorithm
    d = multiplicative_inverse(e, t)
    print(' d: ', d)

    # Return the public and private key_pair
    return ((e, n), (d, n))


def encrypt(public_key_pair, user_message):
    key, n = public_key_pair
    # Encrypt each letter of user_message to numbers based formula:  encryption = message^e mod N
    cipher = [(pow(ord(char), key) % n) for char in user_message]
    #print("cipher=", cipher)
    return cipher


def decrypt(private_key_pair,  cipher):
    key, n = private_key_pair
    # Decrypt the cipher using formula: decryption = encrypted_message^d mode N
    decrypted_value = [str(pow(char, key) % n) for char in cipher]
    # Convert ASCII code to characters
    decrypted_text = [chr(int(char)) for char in decrypted_value]
    return ''.join(decrypted_text)


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