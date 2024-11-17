# user_age = input("Proszę wprowadzić wiek : ")
# print(user_age)

# a = 1
# b = 2
# print('A:', a, ' B:', b)
# print('A: ' + str(a) + " B: " + str(b))
# print(f'A:{a} B:{b}')

# pole = 25.123412351
# print (f"Pole wynosi : { pole:.5f}")
# print(pole)

# print ("a", "b", "c", sep=", ")

# print (" Hello ", end=" ")
# print (" world !")

# print('''
# Pierwsza linijka
#     Druga linijka
#         Trzecia linijka
# ''')

# print(bool('abc'))

# import math 

# a = 10
# b = 3
# print(f'Dodawanie: {a+b}')
# print(f'Odejmowanie: {a-b}')
# print(f'Mnożenie: {a*b}')
# print(f'Dzielenie: {a/b}')
# print(f'Moduł: {a%b}')
# print(f'Potęgowania: {a**b}')
# print(f'Dzielenie całkowite: {a//b}')
# print(f'Pierwiastkowanie: {math.sqrt(10)}')

# print( type(a) is int)

# # a = b
# # a = a + b
# a += b
# print(a)

# i = 1
# while i <= 5:
#     print(i)
#     i += 1

# print(i)

# for x in range (0, 6, 2):
#     print (x)
lista_liczb = [9, 6, 8, 2, 5, 6]
# print(lista_liczb[3:])
# my_list = list ( range (5))

# for i in range(len(lista_liczb)):
# for i in lista_liczb:
#     print(i)

# for iterator, value in enumerate(lista_liczb):
#     print(iterator, value)

# for i in range(len(lista_liczb)):
#     print(i, lista_liczb[i])
# lista_tekst = ['a', 'b', 'c', 'd', 'e']

# for value1, value2 in zip(lista_liczb, lista_tekst):
#     print(value1, value2)

# for i in range(len(lista_liczb)):
#     print(lista_liczb[i], lista_tekst[i])

# print(lista_tekst)
# lista_tekst.append('f')
# print(lista_tekst)
# lista_tekst.extend(['g', 'h', 'i', 'j'])
# print(lista_tekst)

# lista_tekst.insert(1, 'ą')
# print(lista_tekst)

# a = lista_tekst.remove('ą')
# # print(lista_tekst)
# print(a)

# a = lista_tekst.pop()
# print(a)

# lista_liczb.sort(reverse=True)
# print(lista_liczb)

# lista_liczb[0] = 11
# print(lista_liczb)

# krotka_liczb = (5, 4, 7, 6, 0)
# print(krotka_liczb[0])
# print(krotka_liczb[2])
# krotka_liczb[0] = 11

# slownik = {
#     '0': 'A',
#     1: 'B',
#     10: 'C'
# }
# slownik['0'] = 'F'
# print(slownik['0'])
# print(slownik.get('0'))
# a = slownik.pop('0')
# a = slownik.popitem()
# print(a)
# slownik = {}
# print(slownik)
# print(slownik.keys())
# print(slownik.values())
# print(slownik.items())

# print(type(slownik))

# zbior = {1, 2, 3}
# zbior.add(5)
# print(zbior)
# zbior.add(5)
# print(zbior)

# e = zbior.pop()
# print(e)
# e = zbior.pop()
# print(e)
# print(zbior)

# text = "Python jest, super"
# words = text.split(', ')
# print(words)

# sentence = ' '.join(words)
# print(sentence)

# try:
#     number = 0
#     result = 10 / number
#     print(f'Wynik: {result}')
# except ZeroDivisionError as e:
#     print('Wystąpił błąd dzielenia przez 0')
#     print(e)
# except:
#     print('Wystapił błąd') 
# finally:
#     print('Na końcu')

# age = input('Podaj wiek: ')
# if not age.isdigit():
#     raise ValueError (" Wiek nie jest podany jako liczba !")

# age = int(age)

# if age < 10:
#     raise ValueError (" Wiek nie może być mniejszy niż 10 !")

# print('Wiek został podany poprawnie')

# f = open ('file.txt', 'a', encoding ="utf-8")
# with open ('file.txt', 'a', encoding ="utf-8") as plik:
#     # operacje na pliku
#     plik.write('Nowy tekst')

# import os
# import json

# a = 1
# a = 2
# slownik = {
#     'a' : '123'
# }

# slownik_json = {
#     "a": "123",
#     "b": [1, 2, 3],
#     "c": {
#         "d": 1,
#         "e": "3"
#     }
# }

# json_data = json.dumps(slownik_json)
# print(json_data)

# original = " Python strings are COOL! "
# lower_cased = original.lower()
# stripped = original.strip()
# stripped_lower_cased = original.lower().strip()

# # Sprawdźmy czy otrzymaliśmy poprawny wynik
# assert lower_cased == " python strings are cool! "
# assert stripped == "Python strings are COOL!"
# assert stripped_lower_cased == "python strings are cool!"

# ugly = " tiTle of My new Book\n\n"

# pretty = ugly.strip().title()

# assert pretty == "Title Of My New Book"

# verb = "is"
# language = "Python"
# punctuation = "!"

# # Twoja implementacja
# sentence = f"Learning {language} {verb} fun{punctuation}"
# sentence = "Learning {} {} fun{}".format(language, verb, punctuation)

# # Sprawdźmy czy otrzymaliśmy poprawny wynik
# assert sentence == "Learning Python is fun!"

a = 2
b = 3
c = 2

result = 6*(a**3) - ((8*(b**2))/(4*c)) + 11

assert result == 50