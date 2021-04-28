'''def dziwne_dzialanie(liczba1, liczba2):
    suma = liczba1 + liczba2
    kwadrat = suma **2
    wynik = kwadrat - 1
    return wynik, kwadrat

pierwsza = float(input("Podaj pierwszą liczbę "))
druga = float(input("Podaj drugą liczbę "))
wynik, kwadrat = dziwne_dzialanie(pierwsza, druga)
print("Wynikiem skomlikowanego dzialania jest:" ,wynik)
print("Kwadratem podanych liczb jest:" ,kwadrat)'''

#gwiazdki

'''def gwiazdki(liczba_gwiazdek):
    if liczba_gwiazdek > 0:
        print("*")
        gwiazdki(liczba_gwiazdek-1)

gwiazdki(5)'''

#ostatni element rekurancyjnie

'''lista1 = [1,2,3,4,5,6,7,8]

def ostatni(lista):
    print(lista)
    if len(lista)>1:
        return ostatni(lista[1:])
    else:
        return lista

print(ostatni(lista1))'''

#once again

'''def ostatni(lista):
    print(lista)
    if len(lista)>1: #jeśli lista ma więcej niż jeden element
        return ostatni(lista[1:]) #"usuwanie" od początku, po jednym elemencie
    else:
        return lista

print(ostatni([1,45,78,1,7,34,765,0,1,3]))'''

'''def bez_ostatniego(lista):
    nowa_lista = []
    print(lista)
    if len(lista)>1:
        nowa_lista.append(lista[0]) #nowa lista to tylko element pierwszy(pozycja0)
        return nowa_lista + bez_ostatniego(lista[1:])
    else:
        return nowa_lista

print(bez_ostatniego([1,2,3,4,5,6,7,8]))'''

#once again

'''def bez_ostatniego(lista):
    nowa_lista = []
    if len(lista)>1:
        nowa_lista.append(lista[0])
        return nowa_lista + bez_ostatniego(lista[1:])
    else:
        return nowa_lista

print(bez_ostatniego([1,2,3,4,5,6,7,8]))'''

#ogon

'''def ogon(lista):
    nowa_lista = []
    print(lista)
    if len(lista)>1:
        nowa_lista.append(lista[-1])
        return ogon(lista[:-1]) + nowa_lista
    else:
        return nowa_lista

print(ogon([1,2,3,4,5,6,7,8,9]))'''

#minimum

'''def minimum(lista, najmniejszy):
    print(lista)
    if len(lista)>0:
        if lista[0]<najmniejszy:
            najmniejszy = lista[0]
        return minimum(lista[1:], najmniejszy)
    else:
        return najmniejszy

print(minimum([8,4,5,34],8))'''

#maksimum

'''def maksimum(lista, najwiekszy):
    print(lista)
    if len(lista)>0:
        if lista[0]>najwiekszy:
            najwiekszy = lista[0]
        return maksimum(lista[1:], najwiekszy)
    else:
        return najwiekszy

print(maksimum([1,45,98,65,35,67,234,54,786,1,45,9,87],1))'''

#długość

'''def dlugosc(lista):
    print(lista)
    if len(lista)>0:
        return dlugosc(lista[1:]) + 1
    else:
        return 0

print(dlugosc([1,2,3,4,5,6,7,8]))'''

#szukaj

'''def czy_jest(lista,element):
    if len(lista)>0:
        if element == lista[0]:
            return "Element znajduje się na liście"
        else:
            return czy_jest(lista[1:],element)
    else:
        return "Elementu nie ma na liście"

print(czy_jest([1,23,4,5,6,7],12))'''

#n-ta potęga

'''def enta(liczba):
    if liczba > 0:
        return liczba**2
    else:
        return "Liczba nie jest liczbą naturalną"

print(enta(3))'''

#czy są równe

'''def czy_sa(liczba1, liczba2):
    if liczba1 == liczba2:
        return "Liczby są identyczne"
    else:
        różnica = liczba1 - liczba2
        return print("Różnica między liczbami wynosi", różnica)

pierwsza_liczba = int(input("Podaj pierwszą liczbę "))
druga_liczba = int(input("Podaj drugą liczbę "))
wynik = czy_sa(pierwsza_liczba, druga_liczba)
print(wynik)'''
