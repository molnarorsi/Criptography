from PIL import Image
import itertools

def affine_cipher_decrypt(ciphertext, m, b):
    plaintext = bytearray(len(ciphertext))
    for i, char in enumerate(ciphertext):
        plaintext[i] = (m * char + b) % 256
    return bytes(plaintext)

def try_keys(encrypted_image_path):
    with open(encrypted_image_path, 'rb') as f:
        ciphertext = bytearray(f.read())

    # elso 2 bajt
    if ciphertext[:2] != b'\xFF\xD8':
        print("Hiba: Az első két bájt nem felel meg a JPG fájl szignatúrának.")
        return

    # keys komb
    for m, b in itertools.product(range(256), repeat=2):
        decrypted_data = affine_cipher_decrypt(ciphertext, m, b)
        if decrypted_data[:2] == b'\xFF\xD8':
            print("Megfelelő kulcs megtalálva: m = {}, b = {}".format(m, b))
            # A kulcs megtalálása esetén visszatérhetünk, vagy folytathatjuk a további kulcsok keresését

            # A rejtjelezett kép visszafejtése a megtalált kulccsal
            decrypted_image_path = "visszafejtett_kep.jpg"
            with open(decrypted_image_path, 'wb') as decrypted_file:
                decrypted_file.write(decrypted_data)
            print(f"Visszafejtett kép mentve: {decrypted_image_path}")
            return

    print("Nem található megfelelő kulcs.")

def main():
    encrypted_image = 'cryptAffine.jpg'
    try_keys(encrypted_image)

if __name__ == "__main__":
    main()