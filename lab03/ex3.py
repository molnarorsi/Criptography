import string

# Az angol ábécé kisbetűi és a szóköz
alphabet = string.ascii_lowercase + " "

# A blokkméret
d = 2

# A rejtjelezési mátrix
encryption_matrix = [[11, 7], [2, 13]]

# A dekódolási mátrix
decryption_matrix = [[17, 20], [24, 7]]

# A titkosított szöveg beolvasása
with open("outHill.txt", "r") as f:
    ciphertext = f.read().strip()

# A titkosított szöveg feldarabolása blokkokra
blocks = [ciphertext[i:i + d] for i in range(0, len(ciphertext), d)]

# A dekódolt szöveg tárolására
plaintext = ""

# A blokkok dekódolása
for block in blocks:
    # A blokk betűinek dekódolása
    decoded_block = ""
    for i in range(d):
        c = alphabet.index(block[i])
        for j in range(d):
            decoded_block += alphabet[(decryption_matrix[i][j] * c) % 27]

    # A dekódolt blokk hozzáadása a dekódolt szöveghez
    plaintext += decoded_block

# A dekódolt szöveg kiírása
print(plaintext)
