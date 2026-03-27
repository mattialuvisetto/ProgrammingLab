import numpy as np

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    i = 3
    while i * i <= n:   
        if n % i == 0:
            return False
        i += 2          # salta i pari
    return True


a = np.array([2,3,5,7])

print(len(a))
print(a.size)

print(a.dtype)

primes = np.array([n for n in range(2, 10) if is_prime(n)])

print(primes)