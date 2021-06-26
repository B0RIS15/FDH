#fgh - хэш функция, RSA - эцп
from hashlib import sha256
import random

def hashMassage(m):
    return sha256((m).encode()).hexdigest()

def gcd(a, b):
    while b!= 0:
        a, b = b, a % b
    return a

def get_primes(start):
    stop = 65536
    if start > stop:
        return []
    primes = [2]
    for i in range(3, stop - 1, 2):
        for j in primes:
            if i % j == 0:
                break
        else:
            primes.append(i)
    while primes and primes[0] < start:
        del primes[0]
    stop = len(primes)
    start = 0
    while True:
        p = primes[random.randint(0, stop)]
        q = primes[random.randint(0, stop)]
        if p != q:
            break
    return p, q

def moduls(p, q):
    return p * q

def eulerFunction(p, q):
    return (p - 1) * (q - 1)

def publicExponent(F):
    while True:
        e = random.randint(1, F)
        if gcd(e, F) == 1:
            break
    return e

def privateExponent(e, F):
    x, lastx = 0, 1
    a, b = F, e
    while b:
        a, q, b = b, a // b, a % b
        x, lastx = lastx - q * x, x
    d = (1 -lastx * F) // e
    if d < 0:
        d += F
    assert 0 <= d < F and e * d % F == 1
    return d

def encrypt(hashM, e, n):
    r = 1
    hashM = int(hashM, 16)
    while e != 0:
        if e % 2 == 1:
            r = (r * hashM) % n
        e = e // 2
        hashM = (hashM * hashM) % n
    return r

def decrypt(encryptHashM, d, n):
    r = 1
    while d != 0:
        if d % 2 == 1:
            r = (r * encryptHashM) % n
        d = d // 2
        encryptHashM = (encryptHashM * encryptHashM) % n
    return r
                
hashM = 'helloWorld form jupyter notebook'
print(hashMassage(hashM))
#print(len(hashM))
hashM = hashMassage(hashM)
print(hex(int(hashM, 16)))
primes = get_primes(23572)
p = primes[0]
q = primes[1]
print("primes numbers: ", p, q)
F = eulerFunction(p, q)
n = moduls(p, q)
print("moduls: ", n)
print("eulerFun: ", F)
e = publicExponent(F)
print("public exponent: ", e)
d = privateExponent(e, F)
print("private exponent: ", d)
encryptHashM = encrypt(hashM, e, n) 
print("encrypted massege: ", encryptHashM, "\n",hex(encryptHashM))
decryptHashM = decrypt(encryptHashM, d, n)
print("decrypred massage: ", decryptHashM)
