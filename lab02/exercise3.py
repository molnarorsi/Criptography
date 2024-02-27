def extEuclid(a, b):
    if b == 0:                                                              #ha a masodik szam nulla, akkor a lnko az elso szam lesz (0, 1) alakban
        gcd, s, t = a, 1, 0
        return gcd, s, t
    else:
        s2, t2, s1, t1 = 1, 0, 0, 1
        while b > 0:
            q = a // b                                                      #ha a masodik szam nem nulla minden iteracioban kiszamoljuk az r-t(maradekot) a ket szam egesz osztasabol
            r, s, t = (a - b * q), (s2 - q * s1), (t2 - q * t1)             #majd frissitem az erteket u., h. a kovetkezo iteracioban a masodik szam a maradek, az elso szam pedig a korabbi szam lesz
            a, b, s2, t2, s1, t1 = b, r, s1, t1, s, t
        gcd, s, t = a, s2, t2
        return gcd, s, t                                                    #visszateritem a lnko-t es az (s, t)-t


def mInv(a, m):
    g, x, y = extEuclid(a, m)                                               #ha a lnko = 1-el
    if g != 1:                                                              #ha nem akkor nem letezik modularis inverz
        raise Exception('Modular inverse does not exist!!!')
    else:
        return x % m                                                        #ha igen, akkor akkor return x, azaz inverz szam modulo m


def affine_decrypt(ciphertext, a, b):                                       #a es b a kulcsok
    plaintext = ""
    a_inv = mInv(a, 26)                                                  #'a' kulcs modularis inverzenek meghatarozasa
    for char in ciphertext:                                                 #vegigmegyek a szovegen, minden kartakert visszafejtve
        if char.isalpha():                                                  #ha betu akkor visszafejtes tortenik
            if char.isupper():                                              #ha nagybetu, akkor a karakter kodjat atalakitom az angol abc-ben ord(char) - ord('A'), majd levonom az 'A' kodjat, ami megadja hanyadik helyen van az adott karakter az angol abc-ben
                plaintext += chr(((a_inv * (ord(char) - ord('A') - b)) % 26) + ord('A'))
            else:                                                           #ugyanaz kisbetuk eseteben is
                plaintext += chr(((a_inv * (ord(char) - ord('a') - b)) % 26) + ord('a'))        #mind2 esetben az a_inv * ord(char - .... - b resz adja meg a visszafejtett poziciot, es a % 26 muvelettel biztositjuk, h az eredemeny az angol abc-ben maradjon
        else:
            plaintext += char                                               #vegul az 'A' vagy 'a' kodjat hozzaadjuk a vegeredmenyhez
    return plaintext


def comb_affine(ciphertext):                                                #vegigmegy az osszes lehetseges a es b kulcskombinaciokon
    for a in range(1, 26):                                                  #'a' kulcsok (1-25 kozott)
        if extEuclid(a, 26)[0] == 1:                                     #extEuclid fgv-el hatarozom meg az 'a' kulcs es a 26 lnko-jat.
            for b in range(26):                                             #'b' kulcsok (0-25 kozott)
                decrypted_text = affine_decrypt(ciphertext, a, b)
                print(f"a={a}, b={b}: {decrypted_text}")


def main():
    ciphertext = "EX GKLGTGWRGW BE HGDPGAODRG KIRZEX EKIH WIVERREW, RGK VEDRE E PEVOWTE. BGTEWDGIHYAX"
    comb_affine(ciphertext)


if __name__ == "__main__":
    main()

# original text: AZ EMBEREKNEK HA TELJESULNE MINDAZ AMIT KIVANNAK, NEM VALNA A JAVUKRA. HERAKLEITOSZ ; a = 7, b = 4
