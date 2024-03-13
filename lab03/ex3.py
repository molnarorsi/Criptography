import numpy as np

# Alphabet: 26 lowercase letters + space (a=0, b=1, ..., z=25, space=26)
alphabet = "abcdefghijklmnopqrstuvwxyz "
alphabet_index = {char: index for index, char in enumerate(alphabet)}

# Function to convert text to numerical representation
def text_to_numeric(text):
    return [alphabet_index[char] for char in text]

# Function to calculate the modular inverse of a 2x2 matrix modulo 27
def modular_inverse_matrix(matrix, modulus=27):
    determinant = int(np.round(np.linalg.det(matrix))) % modulus
    det_inv = pow(determinant, -1, modulus)
    minors = np.zeros(matrix.shape)
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            minor = np.delete(np.delete(matrix, i, axis=0), j, axis=1)
            minors[i, j] = (-1)**(i+j) * int(np.round(np.linalg.det(minor))) % modulus
    cofactor_matrix = minors.T
    adjugate_matrix = cofactor_matrix
    inverse_matrix = (det_inv * adjugate_matrix) % modulus
    return inverse_matrix

# Function to decrypt text using the inverse matrix
def decrypt_text(numeric_text, inverse_matrix):
    decrypted_numeric = []
    for i in range(0, len(numeric_text), 2):
        block = np.array(numeric_text[i:i+2])
        decrypted_block = np.dot(inverse_matrix, block) % 27
        decrypted_numeric.extend(decrypted_block)
    return ''.join(alphabet[int(index)] for index in decrypted_numeric)

# Load the encrypted text from the file
with open('outHill.txt', 'r') as file:
    encrypted_text = file.read().strip()

# Convert the encrypted text to its numerical representation
encrypted_numeric = text_to_numeric(encrypted_text)

# Known mappings "pu" -> "oa" and "or" -> "we", and their numeric representations
plaintext_pairs = ["pu", "or"]
ciphertext_pairs = ["oa", "we"]
P = np.array([text_to_numeric(pair) for pair in plaintext_pairs]).reshape(2, 2).T
C = np.array([text_to_numeric(pair) for pair in ciphertext_pairs]).reshape(2, 2).T

# Calculate the encryption matrix E and its modular inverse
E = np.dot(C, modular_inverse_matrix(P)) % 27
E_inv = modular_inverse_matrix(E)

# Decrypt the entire text
decrypted_text = decrypt_text(encrypted_numeric, E_inv)

print(decrypted_text)
