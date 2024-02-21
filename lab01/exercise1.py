def caesar_cipher(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            encrypted_text += chr((ord(char) - base + shift) % 26 + base)
        else:
            encrypted_text += char
    return encrypted_text


def caesar_decrypt(encrypted_text, shift):
    return caesar_cipher(encrypted_text, -shift)


def preprocess_text(file_path):
    try:
        with open(file_path, 'r') as file:
            text = file.read()
            text = text.upper()  # Convert to uppercase
            return text
    except FileNotFoundError:
        print("File not found!")
        return None


def main():
    file_path = input("Enter the file path: ")
    shift = int(input("Enter the shift (0-25): "))

    text = preprocess_text('szoveg.txt')
    if text:
        encrypted_text = caesar_cipher(text, shift)
        decrypted_text = caesar_decrypt(encrypted_text, shift)

        print("Encrypted text:")
        print(encrypted_text)
        print("\nDecrypted text:")
        print(decrypted_text)


if __name__ == "__main__":
    main()
