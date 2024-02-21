def caesar_decrypt(text, shift):
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            decrypted_text += chr((ord(char) - base - shift) % 26 + base)
        else:
            decrypted_text += char
    return decrypted_text

def brute_force_decrypt(ciphertext):
    for shift in range(26):
        decrypted_text = caesar_decrypt(ciphertext, shift)
        print(f"Shift = {shift}: {decrypted_text}")

def main():
    ciphertext = "GUR TERRXF BS GUR PYNFFVPNY REN ZNQR FRIRENY ABGNOYR PBAGEVOHGVBAF GB FPVRAPR NAQ URYCRQ YNL GUR SBHAQNGVBAF BS FRIRENY JRFGREA FPVRAGVSVP GENQVGVBAF, YVXR CUVYBFBCUL, UVFGBEVBTENCUL NAQ ZNGURZNGVPF. GUR FPUBYNEYL GENQVGVBA BS GUR TERRX NPNQRZVRF JNF ZNVAGNVARQ QHEVAT EBZNA GVZRF JVGU FRIRENY NPNQRZVP VAFGVGHGVBAF VA PBAFGNAGVABCYR, NAGVBPU, NYRKNAQEVN NAQ BGURE PRAGERF BS TERRX YRNEAVAT JUVYR RNFGREA EBZNA FPVRAPR JNF RFFRAGVNYYL N PBAGVAHNGVBA BS PYNFFVPNY FPVRAPR. TERRXF UNIR N YBAT GENQVGVBA BS INYHVAT NAQ VAIRFGVAT VA CNVQRVN (RQHPNGVBA). CNVQRVN JNF BAR BS GUR UVTURFG FBPVRGNY INYHRF VA GUR TERRX NAQ URYYRAVFGVP JBEYQ JUVYR GUR SVEFG RHEBCRNA VAFGVGHGVBA QRFPEVORQ NF N HAVIREFVGL JNF SBHAQRQ VA PBAFGNAGVABCYR NAQ BCRENGRQ VA INEVBHF VAPNEANGVBAF."
    brute_force_decrypt(ciphertext)

if __name__ == "__main__":
    main()
