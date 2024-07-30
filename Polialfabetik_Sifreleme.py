def polialfabedik_sifrele(metin, parola):
    alfabe_buyuk = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    alfabe_kucuk = 'abcdefghijklmnopqrstuvwxyz'
    
    sifrelenmis_metin = ''
    parola_index = 0
    
    for karakter in metin:
        if karakter.isalpha():
            # kucuk ise
            if karakter.islower():
                index = (alfabe_kucuk.index(karakter) + alfabe_kucuk.index(parola[parola_index % len(parola)])) % 26
                sifrelenmis_metin += alfabe_kucuk[index]
            # buyuk ise
            elif karakter.isupper():
                index = (alfabe_buyuk.index(karakter) + alfabe_kucuk.index(parola[parola_index % len(parola)])) % 26
                sifrelenmis_metin += alfabe_buyuk[index]
            parola_index += 1
        else:
            sifrelenmis_metin += karakter
    return sifrelenmis_metin

# metni iste
metin = input("Lütfen şifrelemek istediğiniz metni girin: ")
parola = input("Lütfen bir parola girin: ")

# sifrele
sifrelenmis_metin = polialfabedik_sifrele(metin, parola)
print("Şifrelenmiş Metin:", sifrelenmis_metin)
