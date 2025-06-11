import math
import random

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def is_perfect_power(n):
    for b in range(2, int(math.log2(n)) + 1):
        a = int(round(n ** (1 / b)))
        if a ** b == n:
            return True
    return False

def order(a, N):
    """Encuentra el menor r tal que a^r ≡ 1 mod N"""
    r = 1
    while pow(a, r, N) != 1:
        r += 1
        if r > N:
            return None
    return r

def shor_classical(N, max_attempts=10):
    if N % 2 == 0:
        return 2
    if is_perfect_power(N):
        return "Perfect power"

    for _ in range(max_attempts):
        a = random.randint(2, N - 2)
        d = gcd(a, N)
        if d > 1:
            return d
        r = order(a, N)
        if r is None or r % 2 != 0:
            continue
        x = pow(a, r // 2, N)
        if x == N - 1 or x == 1:
            continue
        p = gcd(x - 1, N)
        q = gcd(x + 1, N)
        if p * q == N:
            return p, q
    return "Failed to factor"

# Ejemplo de uso
N = 676873
result = shor_classical(N)
print("Factores encontrados:", result)