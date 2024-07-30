def sezar_sifrele(metin, kaydirma):
    sifreli_metin = ""
    for harf in metin:
        # sadece harfleri returnle, diğerlerini atla
        if harf.isalpha():
            #  ASCII degeri al
            ascii_deger = ord(harf)
           
            if harf.isupper():
                sifreli_ascii = (ascii_deger + kaydirma - 65) % 26 + 65
           
            else:
                sifreli_ascii = (ascii_deger + kaydirma - 97) % 26 + 97
            # degerini harfe return et ve şifreli metine ekle
            sifreli_metin += chr(sifreli_ascii)
        else:
            sifreli_metin += harf
    return sifreli_metin


metin = input("Bir metin giriniz : ")
kaydirma = int(input("kaydirma sayisi belirleyiniz : "))

# sifreleme yap
sifreli_metin = sezar_sifrele(metin, kaydirma)
print("Şifrelenmiş Metin:", sifreli_metin)
