from random import randint
from math import pi
from math import sqrt as pierwiastek

############################################################################
print("============================================")
############################################################################

x = 12
y = 4
# print( x / y )

try:
    print(x/y)
    print("Zakonczona dobra linia")
except ZeroDivisionError:
    print("Blad dzielenia przez 0")
except TypeError:
    print("Zle podane dane")
finally:
    print("Wszystko poszlo dobrze! :>")
print("Dalszy wykonywany kod...")


############################################################################
print("============================================")
############################################################################

# print("Losowa wartosc od ... do ...")
# val1 = int(input("wartosc 1: "))
# val2 = int(input("wartosc 2: "))

print("Losowa wartosc od 10 do 100 =====> ", randint(10,100))
print("Pi wynosi ====> ", pi)
print("pierwiastek z 16 ===> ", pierwiastek(16))
print("int pierwiastek z 16 ===> ", int(pierwiastek(16))) 


############################################################################
print("============================================")
############################################################################

def silnia(x):
    if x <= 1:
        return 1
    else:
        return x * silnia(x - 1)

print("Silnia 1: ",silnia(1))
print("Silnia 2: ",silnia(2))
print("Silnia 4: ",silnia(4))
print("Silnia 8: ",silnia(8))
print("Silnia 10: ",silnia(10))

############################################################################
print("============================================")
############################################################################

def dodaj(x,y):
    print("Po dodaniu 10 i 10 wynik: ",x + y)
dodaj(10,10)

############################################################################
print("============================================")
############################################################################

def dodajOdSiebie(x,y):
    print("Po dodaniu: ",x + y)

wartosc1 = int(input("Numer 1: "))
wartosc2 = int(input("Numer 2: "))

dodajOdSiebie(wartosc1,wartosc2)

############################################################################
print("============================================")
############################################################################

def mnozenie(z1,z2):
    return z1 * z2

e1 = int(input("Liczba pierwsza: "))
e2 = int(input("Liczba druga: "))

zmienna = mnozenie(e1,e2)
print("Po przemnożeniu: ",zmienna)

############################################################################
print("============================================")
############################################################################

