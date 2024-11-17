# Zadanie 1.5
# # Twoja implementacja
# x = int(input('Wprowadź liczbę: '))
# result = x / 2 + 4
# # Sprawdźmy czy otrzymaliśmy poprawny wynik
# assert result == 14

# Zadanie 2.1
# x = input('Wprowadź imię: ')
# y = input('Wprowadź nazwisko: ')

# print(f'Cześć {y} {x}')

# Zadanie 2.2
# filename = input('Wprowadź nazwę pliku: ')

# print(filename.split('.'))
# print("Rozszerzenie pliku to:", filename.split('.')[1])
# print(f'Rozszerzenie pliku to: {filename.split(".")[1]}')

# Zadanie 2.3
# dd = input('Podaj dzień: ')
# mm = input('Podaj miesiąc: ')
# yyyy = input('Podaj rok: ')
 
# print(f'{dd}/{mm}/{yyyy}')

# Zadanie 2.4
# x = int(input("podaj liczbe1: "))
# y = int(input("podaj liczbe2: "))
# r = x + y
# print(f'Suma {x} oraz {y} to {r}')

# Zadanie 2.5
# a = int(input("Wprowadź pierwszą liczbę całkowitą: "))
# b = int(input("Wprowadź drugą liczbę całkowitą: "))
# c = float(input("Wprowadź pierwszą liczbę zmiennoprzecinkową: "))
# d = float(input("Wprowadź drugą liczbę zmiennoprzecinkową: "))

# wynik1 = a+c
# wynik2 = d-b

# print(f"Wynik operacji 1: {wynik1}")
# print(type(wynik1))
# print(f"Wynik operacji 2: {wynik2}")
# print(type(wynik2))

# suma = wynik1 + wynik2

# print(f"Suma to: {suma}")
# print(type(suma))

# Zadanie 2.6
# liczba = int(input('Podaj liczbe: '))
# stopien = int(input('Podaj stopien pierwiastka: '))

# print(f'Wynik to {liczba**(1/stopien)}')
# print(f'Pierwiastek stopnia {stopien} z {liczba} to {liczba**(1/stopien)}')
# print(f'{(0.1+0.2):.2f}')

# Zadanie 2.7
# słowo1 = str(input("podaj słowo:"))
# słowo2 = str(input("podaj słowo:"))

# print(f'{słowo1} {słowo2}')
# print(słowo1, słowo2, sep=", ")
# print(słowo1, end=" ")
# print(słowo2)

# txt1 = input("podaj tekst 1: ")
# txt2 = input("Podaj tekst 2: ")

# print (f"1. {txt1} {txt2}")
# print("2.", txt1, txt2)
# print("3. " + txt1 + " " + txt2)
# print("4.", txt1, end=" ")
# print(txt2)

# Zadanie 2.8
# a = float(input('Podaj pierwszy bok: '))
# b = float(input('Podaj drugi bok: '))
# c = float(input('Podaj trzeci bok: '))
 
# p = (a + b + c) / 2
 
# pole = (p * (p - a) * (p - b) * (p - c)) ** 0.5
 
# print(f'Pole trójkąta wynosi: {pole:.2f}')

# Zadanie 2.9
# km = float(input('Podaj wartość w kilometrach: '))
# mile = 0.621371192 * km
 
# print(f'{km:.2f} kilometra to {mile:.2f} mili')

# Zadanie 2.10
# cel = float(input("Podaj temperaturę w Celsjuszach: "))
# fahr = (cel * 9 / 5) + 32
 
# print(f"{cel:.1f} stopni celsjusza to {fahr:.1f} stopni Fahrenheita")