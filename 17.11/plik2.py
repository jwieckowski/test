# Zadanie 1.1.1
# Stwórzmy pustą listę
# my_list = []
 
# # Dodajmy wartości
# my_list.append("Python")
# my_list.append("is ok")
# my_list.append("sometimes")
 
# # Usuńmy 'sometimes'
# my_list.remove("sometimes")
 
# # Zmieńmy drugi element listy
# my_list[1] = "is neat"
 
# # Sprawdźmy czy otrzymaliśmy poprawny wynik
# assert my_list == ["Python", "is neat"]

# Zadanie 1.1.2
# original = ["I", "am", "learning", "hacking", "in"]
# Twoja implementacja
# v1
# modified = original[:]
# modified.append("Python")
# modified[3] = "lists"
# v2
# modified = original.copy()
# modified.append("Python")
# modified[3] = "lists"
# v3
# modified = [*original, 'Python']
# modified[3] = "lists"

# # Sprawdźmy czy otrzymaliśmy poprawny wynik
# assert original == ["I", "am", "learning", "hacking", "in"]
# assert modified == ["I", "am", "learning", "lists", "in", "Python"]

# Zadanie 1.1.3
# list1 = [6, 12, 5]
# list2 = [6.2, 0, 14, 1]
# list3 = [0.9]

# v1
# combo = list1 + list2 + list3
# my_list = sorted(combo, reverse=True)
# v2
# my_list = list1.copy()
# my_list.extend(list2)
# my_list.extend(list3)
# my_list = sorted(my_list, reverse=True)
# v3
# my_list = sorted([list1, list2, list3], reverse=True)

# assert my_list == [14, 12, 6.2, 6, 5, 1, 0.9, 0]

# Zadanie 1.2.1
# first_name = "John"
# last_name = "Doe"
# favorite_hobby = "Python"
# sports_hobby = "gym"
# age = 82

# my_dict = {
#     "name": f"{first_name} {last_name}",
#     "age": age, 
#     "hobbies": [favorite_hobby,sports_hobby]
# }

# assert my_dict == {"name": "John Doe", "age": 82, "hobbies": ["Python", "gym"]}

# Zadanie 1.2.2
# dict1 = dict(key1="This is not that hard", key2="Python is still cool")
# dict2 = {"key1": 123, "special_key": "secret"}
# # Można również zainicjalizować słownik przez wykorzystanie listy krotek
# dict3 = dict([("key2", 456), ("keyX", "X")])

# # Twoja implementacja
# my_dict = {**dict1, **dict2, **dict3}
# special_value = my_dict.pop('special_key')
# special_item = my_dict.popitem()

# # Sprawdźmy czy otrzymaliśmy poprawny wynik
# assert my_dict == {"key1": 123, "key2": 456, "keyX": "X"}
# assert special_value == "secret"

# # Sprawdźmy czy słowniki początkowe nie zostały zmienione
# assert dict1 == {"key1": "This is not that hard", "key2": "Python is still cool"}
# assert dict2 == {"key1": 123, "special_key": "secret"}
# assert dict3 == {"key2": 456, "keyX": "X"}

# Zadanie 1.3.1
# name = "John"

# if len(name) > 20:
#     print(f'Name "{name}" is more than 20 chars long')
#     length_description = "long"
# elif len(name) > 15:
#     print(f'Name "{name}" is more than 15 chars long')
#     length_description = "semi long"
# elif len(name) > 10:
#     print(f'Name "{name}" is more than 10 chars long')
#     length_description = "semi long"
# elif len(name) in range(8, 11):
#     print(f'Name "{name}" is 8, 9 or 10 chars long')
#     length_description = "semi short"
# else:
#     print(f'Name "{name}" is a short name')
#     length_description = "short"

# # Sprawdźmy czy otrzymaliśmy poprawny wynik
# assert length_description == "semi short"

# Zadanie 1.3.2
# words = ["PYTHON", "JOHN", "chEEse", "hAm", "DOE", "123"]
# upper_case_words = []
# for word in words:
#     if word.isupper():
#         upper_case_words.append(word)

# # Sprawdźmy czy otrzymaliśmy poprawny wynik
# assert upper_case_words == ["PYTHON", "JOHN", "DOE"]
# upper_case_words = [word for word in words if word.isupper()]
# upper_case_words = [i if i.isupper() else 1 for i in words]
# print(upper_case_words)

# Zadanie 1.3.3
# magic_dict = dict(val1=44, val2="secret value", val3=55.0, val4=1)
# # Twoja implementacja
# # sum_of_values = sum([magic_dict[key] for key in magic_dict.keys() if isinstance(magic_dict[key],(int, float))])
# sum_of_values = 0
# for key in magic_dict.keys():
#     if isinstance(magic_dict[key],(int, float)):
#         sum_of_values += magic_dict[key]

# # Sprawdźmy czy otrzymaliśmy poprawny wynik
# assert sum_of_values == 100

# Zadanie 1.3.4
# numbers = [1, 3, 4, 6, 81, 80, 100, 95]
# # Twoja implementacja
# my_list = []
# for number in numbers:
#     if number % 5 == 0 and number % 2 == 1:
#         my_list.append("five odd")
#     elif number % 5 == 0 and number % 2 == 0:
#         my_list.append("five even")
#     elif number % 2 == 1:
#         my_list.append("odd")
#     elif number % 2 == 0:
#         my_list.append("even")

# # Sprawdźmy czy otrzymaliśmy poprawny wynik
# assert my_list == [
#     "odd",
#     "odd",
#     "even",
#     "even",
#     "odd",
#     "five even",
#     "five even",
#     "five odd",
# ]

# Zadanie 2.1
# 90 - 100
# 75 - 89
# 65 - 74
# 60 - 64
# 50 - 59
# 0 - 49
# score = {
#     (90, 100): 5.0,
#     (75, 89): 4.5,
#     (65, 74): 4.0,
#     (60, 64): 3.5,
#     (50, 59): 3.0,
#     (0, 49): 2.0
# }
 
# punkty = int(input("Podaj liczbę punktów: "))
 
# ocena = None
# for przedzial, ocena_wynik in score.items():
#     if przedzial[0] <= punkty <= przedzial[1]:
#         ocena = ocena_wynik
#         break
 
 
# print(f"Liczba punktów: {punkty}")
# print(f"Uzyskana ocena: {ocena}")
# if ocena >= 3.0:
#     print("Student zaliczył zadanie")
# else:
#     print("Student nie zaliczył zadania")

# Zadanie 2.2
# month = input("Wprowadź miesiąc: ")
 
# seasons = {
#     '1': 'zima', 'styczeń': 'zima',
#     '2': 'zima', 'luty': 'zima',
#     '3': 'zima', 'marzec': 'zima',
#     '4': 'wiosna', 'kwiecien': 'wiosna',
#     '5': 'wiosna', 'maj': 'wiosna',
#     '6': 'wiosna', 'czerwiec': 'wiosna',
#     '7': 'lato', 'lipiec': 'lato',
#     '8': 'lato', 'sierpień': 'lato',
#     '9': 'lato', 'wrzesień': 'lato',
#     '10': 'jesień', 'październik': 'jesień',
#     '11': 'jesień', 'listopad': 'jesień',
#     '12': 'jesień', 'grudzień': 'jesień'
# }

# print(seasons[month] if month in seasons.keys() else "Podano miesiąc poza zakresem")
# v2
# month = input("Wprowadź miesiąc: ")
# seasons = {
#     ('1', '2', '3', 'styczeń', 'luty', 'marzec'): "zima",
#     ('4', '5', '6', 'kwiecień', 'maj', 'czerwiec'): "wiosna",
#     ('7', '8', '9', 'lipiec', 'sierpień', 'wrzesień'): "lato",
#     ('10', '11', '12', 'październik', 'listopad', 'grudzień'): "jesień",
# }
# # season = None
# # for key, value in seasons.items():
# #     if month in key:
# #         season = value
# #         break

# season = [value for key, value in seasons.items() if month in key][0]

# print(f'Pora roku dla miesiąca {month}: {season}')

# Zadanie 2.3
# lista = ['tekst', 1, 1.5, True, [0]]
# print(len(lista))
# print(lista[0])
# print(lista[len(lista)//2])
# print(lista[len(lista)-1]) # print(lista[-1])
# print(lista)
# lista.insert(0, 'Pierwszy')
# lista.append('Ostatni')
# print(lista)

# Zadanie 2.4
# v1
# lista = [x for x in range(1,11)]
# # v2
# # lista = list(range(1,11))
# print(lista)
 
# lista.sort(reverse = True)
# print(lista)
 
# nowa_lista = lista[:5]
# print(nowa_lista)
 
# nowa_lista.remove(nowa_lista[len(nowa_lista)//2])
# print(nowa_lista)
 
# nowa_lista.sort()
# print(nowa_lista)

# element = 8
 
# if element in lista:
#     print(f'W pierwszej liście występuje element {element}')
# else:
#     print('Nie istnieje')

# if element in nowa_lista:
#     print(f'W nowej liście występuje element {element}')
# else:
#     print('Nie istnieje')
 
# del lista
# del nowa_lista

# print(lista)

# Zadanie 2.5
# licz1 = float(input("Podaj pierwszą liczbę: "))
# licz2 = float(input("Podaj drugą liczbę: "))
# operator = input("Podaj operator (+, -, *, /): ")

# # if operator == '+':
# #     wynik = licz1 + licz2
# # elif operator == '-':
# #     wynik = licz1 - licz2
# # elif operator == '*':
# #     wynik = licz1 * licz2
# # elif operator == '/':
# #     wynik = licz1 / licz2
# # else:
# #     wynik = "Nieznany operator"

# operators = {
#     '+': licz1 + licz2,
#     '-': licz1 - licz2,
#     '*': licz1 * licz2,
#     '/': licz1 / licz2
# }

# dzialanie = f"{licz1} {operator} {licz2}"

# # Wyświetlenie wyniku
# print(f"Działanie: {dzialanie}")
# if operator not in operators.keys():
#     print('Nieznany operator')
# else:
#     print(f"Wynik: {operators[operator]}")

# Zadanie 2.6
# z= input("Podaj pełne działanie: ")
# lis=z.split()
 
# x=float(lis[0])
# y=float(lis[2])
# k=lis[1]
 
 
# dzialania = {
#     "+": x + y,
#     "*": x*y,
#     "-": x - y,
#     "/": x/y,
# }
 
# wynik = [value for key, value in dzialania.items() if k in key][0]
# print(f"Działanie {z}")
# print(f"Wynik {wynik}")

# Zadanie 2.7
# lista = [-4, -3, -2, -1, 0, 3, 6, 9, 12]
# print([value for value in lista if value > 0])

# Zadanie 2.8
# wynik = [(i, 1, i, i**2, i**3) for i in range(11)]
# print(wynik)

# Zadanie 2.9
# lista = [22, 19, 24, 25, 26, 24, 25, 24]
# zbior = set(lista)
# print(len(lista),len(zbior))
# print(lista if len(lista) > len(zbior) else zbior)

# Zadanie 2.10
# x = int(input('Podaj liczbę: '))
 
# for y in range(1, 11):  print(f'{x} * {y} = {x * y}')

# Zadanie 2.11
# suma_parzyste = sum(i for i in range(101) if i % 2 == 0)
# suma_nieparzyste = sum(i for i in range(101) if i % 2 == 1)
 
# print(f'Suma liczb parzystych: {suma_parzyste}')
# print(f'Suma liczb nieparzystych: {suma_nieparzyste}')

# Zadanie 2.12
# tekst = '"Uczę się Pythona, aby móc tworzyć aplikacje. Dużą zaletą Pythona jest to że jest bardzo zbliżony do języka angielskiego. Posiada prostą składnię, ale czasami potrafi być skomplikowany przez wysoki poziom abstrakcji. Jednak dobrze jest się nauczyć Pythona, aby dalej rozwijać się w stronę programowania."'
# zdania = tekst.split('. ')

# for zdanie in zdania:
#     print(zdanie)
#     slowa = zdanie.split(' ')
#     print(f'Liczba unikalnych słów: {len(set(slowa))}')
#     print(f'Liczba słów: {len(slowa)}')

# Zadanie 2.13
# X = [
#     [12,9,3],
#     [4,5,6],
#     [7,8,3]
# ]
# Y = [
#     [9,8,1],
#     [6,7,3],
#     [4,5,9]
# ]

# result = []
# for i in range(len(X)):
#     row = []
#     for j in range(len(X[i])):
#         row.append(X[i][j] + Y[i][j])
#     result.append(row)

# assert result == [[21, 17, 4], [10, 12, 9], [11, 13, 12]]

# Zadanie 2.14
X = [
    [12,9],
    [7 ,3],
    [5 ,6]
]

result = [
    [0, 0, 0],
    [0, 0, 0]
]

for i in range(len(result)):
    for j in range(len(result[i])):
        result[i][j] = X[j][i]

assert result == [[12, 7, 5], [9, 3, 6]]

