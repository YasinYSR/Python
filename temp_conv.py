print("-"*30)
print("1.) C --> F")
print("2.) F --> C")
print("3.) C --> K")
print("4.) K --> C")
print("-"*30)

choice=int(input("Seciminiz(1/2/3/4): "))

if choice==1:
    print("\n C --> F")
    celsius=float(input("Deger: "))
    fahrenheit=(celsius*1.8)+32
    print("{} C derece {} F dereceye eşittir.".format(celsius,fahrenheit))
elif choice==2:
    print("\n F --> C")
    fahrenheit=float(input("Değer: "))
    celsius=(fahrenheit-32)/1.8
    print("{} F derece {} C dereceye eşittir.".format(celsius,fahrenheit))
elif choice==3:
    print("\n C --> K")
    celsius=float(input("Değer: "))
    kelvin=celsius+273
    print("{} C derece {} K dereceye eşittir".format(celsius,kelvin))
elif choice==4:
    print("\n K --> C")
    kelvin=float(input("Değer: "))
    celsius=kelvin-273
    print("{} K derece {} C dereceye eşittir.".format(kelvin,celsius))
else:
    print(" _*ERROR*_ "*1000000)