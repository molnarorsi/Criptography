def caesar_cipher_byte(byte, shift):
    # A Caesar titkosítás módosítja a bájtok értékét az eltolásnak megfelelően
    return (byte + shift) % 256


def caesar_decrypt_byte(byte, shift):
    # A Caesar titkosítás visszafejtése az eredeti bájtok helyreállítását jelenti
    return (byte - shift) % 256


def caesar_cipher_file(input_file, output_file, shift):
    with open(input_file, 'rb') as f_input:
        with open(output_file, 'wb') as f_output:
            byte = f_input.read(1)
            while byte:
                encrypted_byte = caesar_cipher_byte(ord(byte), shift)
                f_output.write(bytes([encrypted_byte]))
                byte = f_input.read(1)


def caesar_decrypt_file(input_file, output_file, shift):
    with open(input_file, 'rb') as f_input:
        with open(output_file, 'wb') as f_output:
            byte = f_input.read(1)
            while byte:
                decrypted_byte = caesar_decrypt_byte(ord(byte), shift)
                f_output.write(bytes([decrypted_byte]))
                byte = f_input.read(1)


def main():
    input_file = "input.bin"
    encrypted_file = "encrypted.bin"
    decrypted_file = "decrypted.bin"
    shift = 3  # A Caesar titkosítás eltolása

    # Bináris állomány titkosítása
    caesar_cipher_file(input_file, encrypted_file, shift)
    print(f"File '{input_file}' encrypted to '{encrypted_file}' with Caesar shift {shift}.")

    # Bináris állomány visszafejtése
    caesar_decrypt_file(encrypted_file, decrypted_file, shift)
    print(f"File '{encrypted_file}' decrypted to '{decrypted_file}' with Caesar shift {shift}.")


if __name__ == "__main__":
    main()