# değer: 4

metin = input("Metin Giriniz: ")

kaynak = "abcçdefgğhıijklmnoöprsştuüvyz"
hedef = "defgğhıijklmnoöprsştuüvyzabcç"

coder = str.maketrans(kaynak, hedef)
decoder = str.maketrans(hedef, kaynak)

cod = metin.translate(coder)

print(metin.translate(coder))
print(cod.translate(decoder))