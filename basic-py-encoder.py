#!/usr/bin/env python3
import numpy as np
import string

# encode - plaintext is reversed, inserted every odd position and surrounded by padding
def encode(plaintext):
    payload = ''
    plaintext = plaintext[::-1]
    length = len(plaintext)
    padding = np.random.choice(list(string.ascii_letters + string.digits + string.punctuation), length)
    for i in range(length):
        payload = payload + plaintext[i] + padding[i]
    # Always append additional padding when plaintext is odd length
    if length % 2 != 0:
        payload = np.random.choice(list(string.ascii_letters + string.digits + string.punctuation), 1)[0] + payload
    return payload

# decode - plaintext is extracted on odd positions and then reversed
def decode(payload):
    plaintext = ''
    for i in range(len(payload)):
        if i % 2 != 0:
            plaintext = plaintext + payload[i]
    plaintext = plaintext[::-1]
    return plaintext

plaintext = 'Android'
payload = encode(plaintext)
print(f"{plaintext} is encoded as {payload}")

# padding = '5d;ijo(rqd,nrA('
plaintext = decode(payload)
print(f"{payload} is decoded as {plaintext}")
