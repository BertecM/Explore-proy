import math
from itertools import permutations

def decrypt_transposition(cipher_text, key):
    n_cols = len(key)
    n_rows = math.ceil(len(cipher_text) / n_cols)
    n_shaded_boxes = (n_cols * n_rows) - len(cipher_text)

    # Crear un array con columnas vacías
    cols = [''] * n_cols
    col_lengths = [n_rows] * n_cols

    # Ajustar longitudes de columnas si hay celdas vacías
    for i in range(n_shaded_boxes):
        col_lengths[-(i + 1)] -= 1

    # Llenar columnas con caracteres del texto cifrado
    pos = 0
    for idx in key:
        length = col_lengths[idx]
        cols[idx] = cipher_text[pos:pos+length]
        pos += length

    # Reconstruir texto por filas
    plaintext = ''
    for i in range(n_rows):
        for col in cols:
            if i < len(col):
                plaintext += col[i]
    return plaintext
# Texto cifrado (reemplázalo por tu mensaje)
cipher_text = "pcceellndaalrvvaioictutaonobecahzabialcjdvdkeielutfmnogn"

# Clave de transposición (como orden de columnas, ej: [0,1,2,3] o alguna permutación de eso)
# Si no conoces la clave, puedes probar todas las permutaciones de longitud n
for perm in permutations(range(8)):
    plain = decrypt_transposition(cipher_text, perm)
    print(f"Clave {perm} → {plain}")