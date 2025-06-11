import random
import string

cipher_text = "yuerlgaqrvooazhezlwrs"
alphabet = string.ascii_lowercase
char_to_index = {char: idx for idx, char in enumerate(alphabet)}
index_to_char = {idx: char for idx, char in enumerate(alphabet)}

def decrypt_caesar_with_matrix(cipher, matrix):
    decrypted = ""
    for i, char in enumerate(cipher):
        shift = matrix[i % len(matrix)]
        decrypted_index = (char_to_index[char] - shift) % 26
        decrypted += index_to_char[decrypted_index]
    return decrypted

# Probar 2000 matrices aleatorias de longitud 7
for _ in range(2000):
    matrix = [random.randint(0, 25) for _ in range(7)]
    decrypted = decrypt_caesar_with_matrix(cipher_text, matrix)
    if sum(decrypted.count(c) for c in 'aeos ') >= 5:
        print("Matriz:", matrix, "→", decrypted)