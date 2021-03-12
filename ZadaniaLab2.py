import  sys as  system

#ZAD1

print("\nZadanie1\n")

Zdanie = input("Podaj zdanie zawierające literę 'a' ")

print(Zdanie.count("a"))

#ZAD2

print("\nZadanie2\n")

system.stdout.write("Podaj liczbę a: ")
a = int(system.stdin.readline())

system.stdout.write("Podaj liczbę b: ")
b = int(system.stdin.readline())

system.stdout.write("Podaj liczbę c: ")
c = int(system.stdin.readline())

wynik = str((a ** b) + c)

system.stdout.write(wynik)

#ZAD 3

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

#ZAD 4

print("\nZadanie4\n")

lista = [2, 3, 4, 5.5, 7.5]

for number in lista:
    kwadrat = [number ** 2]
    print(kwadrat)

#ZAD 5

print("\nZadanie5\n")

z = 0
while z !=10:
    print(z)
    z += 2
lista = [z]











