#!/usr/bin/env python3
import numpy as np
import string

# encode - plaintext is reversed, inserted every odd position and surrounded by ciphertext
def encode(plaintext):
    ciphertext = ''
    plaintext = plaintext[::-1]
    length = len(plaintext) 
    padding = np.random.choice(list(string.ascii_letters + string.digits + string.punctuation), length)
    for i in range(length):
        ciphertext = ciphertext + plaintext[i] + padding[i]
    # Always append additional cipher text when plaintext is odd length
    if length % 2 != 0:
        ciphertext = np.random.choice(list(string.ascii_letters + string.digits + string.punctuation), 1)[0] + ciphertext
    return ciphertext

# decode - plaintext is extracted on odd positions and then reversed
def decode(ciphertext):
    plaintext = ''
    for i in range(len(ciphertext)):
        if i % 2 != 0:
            plaintext = plaintext + ciphertext[i]
    plaintext = plaintext[::-1]
    return plaintext

plaintext = 'Android'
ciphertext = encode(plaintext)
print(f"{plaintext} is encoded as {ciphertext}")

# ciphertext = '5d;ijo(rqd,nrA('
plaintext = decode(ciphertext)
print(f"{ciphertext} is decoded as {plaintext}")
