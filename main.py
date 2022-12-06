import random
from random import shuffle
import string

while True:
    stringamount = int(input("Hvor mange bogstaver ønsker du i din adgangskode?\nSkriv her: "))
    intamount = int(input("Hvor mange tal ønsker du i din adgangskode?\nSkriv her: "))
    specialamount = int(input("Hvor mange specielle tegn ønsker du i din adgangskode?\nSkriv her: "))

    strings = ""
    ints = ""
    specials = ""

    while stringamount > 0:
        letter = random.choice(string.ascii_letters)
        strings += letter
        stringamount -= 1

    while intamount > 0:
        number = random.choice(str(123456789))
        ints += str(number)
        intamount -= 1

    while specialamount > 0:
        special = random.choice("_-@#$%&/")
        specials += special
        specialamount -= 1

    passwordstogether = strings + ints + specials

    finalpassword = ''.join(random.sample(passwordstogether,len(passwordstogether)))

    print("\n\n\nVærsgo'! Her er dit nye password!\n")
    print(finalpassword)

    startagain = input("\n\n\nTryk Enter for at generere en ny kode.\n\n\n")

    if startagain != "":
        quit()