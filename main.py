import  sys as  system
import cmath

#ZAD1
print("Zadanie 1\n")
a = 5
b = 3.14

print(a)
print(b)


#ZAD2

print("\nZadanie 2\n")

dodawanie = 5 + 6
odejmowanie = 7 - 3
mnożenie = 8 * 8
dzielenie = 12 / 6
potęgowanie = 3 ** 2
reszta = 8 % 3

print(dodawanie)
print(odejmowanie)
print(mnożenie)
print(dzielenie)
print(potęgowanie)
print(reszta)

#ZAD3

print("\nZadanie 3\n")

Działanie1 = cmath.e ** 10
print(Działanie1)

#ZAD4

print("\nZadanie 4\n")

Imie = "ERYK"
Nazwisko = "POREDA"
print(Imie.capitalize())
print(Nazwisko.capitalize())

#ZAD5

print("\nZadanie 5\n")

Piosenka = "la la la la la"
Liczba = Piosenka.count("la")
print(Liczba)

#ZAD6

print("\nZadanie 6\n")

zmienna1 = "Pochmurna pogoda"
print(zmienna1[0])
print(zmienna1[15])

#ZAD7

print("\nZadanie 7\n")

print(zmienna1.split())

#ZAD8

print("\nZadanie 8\n")

string = "Sosna"
float = 3.14
szesnastkowy = hex(3435)
print(string)
print(float)
print(szesnastkowy)

#ZAD9

print("\nZadanie 9\n")

lista = ["Koszykówka", "Piłka Nożna", "Tenis", "Tenis Stołowy", "Skok w dal" ]
lista.reverse()
print(lista)
lista.extend(("Biegi przełajowe", "Siatkówka", "Bieg na 100m"))
print(lista)

#ZAD10

print("\nZadanie 10\n")

slownik = {}
slownik["prof."] = "profesor"
slownik["ul."] = "ulica"
slownik["r-k"] = "rachunek"
slownik["wg"] = "według"

print(slownik)



#ZAD11

print("\nZadanie1\n")

Zdanie = input("Podaj zdanie zawierające literę 'a' ")

print(Zdanie.count("a"))

#ZAD12

print("\nZadanie2\n")

system.stdout.write("Podaj liczbę a: ")
a = int(system.stdin.readline())

system.stdout.write("Podaj liczbę b: ")
b = int(system.stdin.readline())

system.stdout.write("Podaj liczbę c: ")
c = int(system.stdin.readline())

wynik = str((a ** b) + c)

system.stdout.write(wynik)

#ZAD 13

print("\nZadanie3\n")

a = input("Wprowadz liczbe a: ")
b = input("Wprowadz liczbe b: ")
c = input("Wprowadz liczbe c: ")

a = int(a)
b = int(b)
c = int(c)

if (a > b) & (a > c):
    print("Liczba " + str(a) + " jest największa")

if (b > a) & (b > c):
    print("Liczba " + str(b) + " jest największa")

if (c > b) & (c > b):
    print("Liczba " + str(c) + " jest największa")

#ZAD 14

print("\nZadanie4\n")

lista = [2, 3, 4, 5.5, 7.5]

for number in lista:
    kwadrat = [number ** 2]
    print(kwadrat)

#ZAD 15

print("\nZadanie5\n")

z = 0
while z !=10:
    print(z)
    z += 2
lista = [z]











