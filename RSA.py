import math

def egcd(a, b):
    if a == 0:
        return b, 0, 1
    g, y, x = egcd(b % a, a)
    return g, x - (b // a) * y, y

def modinv(a, m):
    g, x, _ = egcd(a, m)
    if g != 1:
        raise Exception('No inverse')
    return x % m

def rsa_decrypt(c, e, N):
    # Paso 1: Factorizar N
    for p in range(2, int(math.isqrt(N)) + 1):
        if N % p == 0:
            q = N // p
            break
    else:
        raise Exception("No se pudo factorizar N")

    print(f"Factores encontrados: p = {p}, q = {q}")

    # Paso 2: Calcular phi(N)
    phi = (p - 1) * (q - 1)

    # Paso 3: Calcular d (inverso modular de e mod phi)
    d = modinv(e, phi)
    print(f"Exponente privado d = {d}")

    # Paso 4: Descifrar mensaje
    m = pow(c, d, N)
    return m

# Datos
e = 66139
N = 1914401
c = 7

mensaje_descifrado = rsa_decrypt(c, e, N)
print(f"Mensaje descifrado (como número): {mensaje_descifrado}")