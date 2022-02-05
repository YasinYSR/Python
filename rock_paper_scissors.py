import random as rd

print("-"*20+"\nTaş, Kağıt, Makas\n"+"-"*20)

CompScr,UsrScr=0,0

while True:
    print("\n1-) Taş\n2-) Kağıt\n3-) Makas\nÇıkmak için herhangi bir tuşa basın")
    usr_choice=input("Seçiminiz: ")
    com_choice=rd.choice(["1","2","3"])
    if usr_choice=="1":
        if com_choice=="1":
            print("Bilgisayarın seçimi: Taş\nOyuncunu Seçimi: Taş\n     Berabere...")
        elif com_choice=="2":
            print("Bilgisayarın seçimi: Kağıt\nOyuncunu Seçimi: Taş\n     Bilgisayar Kazandı")
            CompScr+=100
        elif com_choice=="3":
            print("Bilgisayarın seçimi: Makas\nOyuncunu Seçimi: Taş\n     Oyuncu Kazandı")
            UsrScr+=100
    elif usr_choice=="2":
        if com_choice=="1":
            print("Bilgisayarın seçimi: Taş\nOyuncunu Seçimi: Kağıt\n     Oyuncu Kazandı")
            UsrScr+=100
        elif com_choice=="2":
            print("Bilgisayarın seçimi: Kağıt\nOyuncunu Seçimi: Kağıt\n     Berabere...")
        elif com_choice=="3":
            print("Bilgisayarın seçimi: Makas\nOyuncunu Seçimi: Kağıt\n     Bilgisayar Kazandı")
            CompScr+=100
    elif usr_choice=="3":
        if com_choice=="1":
            print("Bilgisayarın seçimi: Taş\nOyuncunu Seçimi: Makas\n     Bilgisayar Kazandı")
            CompScr+=100
        elif com_choice=="2":
            print("Bilgisayarın seçimi: Kağıt\nOyuncunu Seçimi: Makas\n     Oyuncu Kazandı")
            UsrScr+=100
        elif com_choice=="3":
            print("Bilgisayarın seçimi: Makas\nOyuncunu Seçimi: Makas\n     Berabere...")
    else:
        break

print("\nOyuncu Skor: {}\nBilgisayar Skor: {}".format(UsrScr,CompScr))