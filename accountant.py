"""a) python accountant.py saldo <int wartosc> <str komentarz>
b) python accountant.py sprzedaż <str identyfikator produktu> <int cena> <int liczba sprzedanych>
c) python accountant.py zakup <str identyfikator produktu> <int cena> <int liczba zakupionych>
d) python accountant.py konto
e) python accountant.py magazyn <str identyfikator produktu 1> <str identyfikator produktu 2> <str identyfikator produktu 3> ...
f) python accountant.py przegląd"""

import sys

akcja= ["saldo", "sprzedaz", "zakup", "konto", "magazyn", "przeglad", "stop"]
saldo = 0
sprzedaz = 0
zakup = 0
konto = ""          # sprawdzic - po co to definiowac tu?
magazyn = {}        # slownik
historia = []       # lista wyswietlana w przeglad
stop = True
komentarz = True    # przydatne do anulowania transakcji na poziomie komentarza w saldzie
wartosc = 0         # poczatkowe saldo na koncie
stan_konta = 0      # tu przechowuje aktualne saldo
cena = 0            # def ceny produktu
wartosc_produkt = 0 # wartosc kupionego produktu (cena * ilosc)


while True:
    print('#' * 87)
    print(f'Dostepne akcje: {akcja}\nCo wybierasz?')  # jak w 1 lini te 3 printy?
    print('#' * 87)

    wybor = str(input())

    if wybor not in akcja:
        print("Zły wybor. Jeszcze raz")
        continue

    if wybor == "saldo":
        print('/jestesmy w saldo/')
        print('podaj wartosc transakcji')

        wartosc = int(input())


# or stan_konta > wartosc:
        if wartosc <= 0 and stan_konta == 0:
            print('Zla kwota, brak mozliwosci wyplaty')
            continue

        print('podaj komentarz do transakcji - (STOP=anulowanie transakcji)')
        komentarz = str(input())

        if komentarz == "stop":
            print("Transakcja anulowana")
            continue

        stan_konta += wartosc
        historia_saldo = (wartosc, komentarz)
        historia.append(historia_saldo)
        continue

    if wybor == "zakup":
        print('/jestesmy w zakup/')

        print('podaj ID produktu:')
        produkt = str(input())


        print('podaj cene jednostkowa produktu:')
        cena = int(input())
        if cena <= 0:
            print('Zla cena!')
            continue

        if cena > stan_konta:
            print('Brak srodkow na zakup')
            break

        print('podaj ilosc sztuk produktu:')
        ilosc = int(input())

        if ilosc <=0 or ilosc * cena > stan_konta:
            print('Brak srodkow na zakup')
            break

        stan_konta -= cena * ilosc
        wartosc_produkt = cena * ilosc

# zle oblicza wartośc w przegladzie jesli wczesniej były w saldo  minusy (wyplaty)
# rozdzielic na wartosc_zakup oraz wartosc_sprzedaz ???



# printa ponizej poprawic
#        print(f,"Kupiono",{sztuk}, {produkt}, "o wartosci:", {wartosc_produkt})

        if produkt in magazyn:
            magazyn[produkt] += ilosc
        else:
            magazyn[produkt] = ilosc

        historia_zakup = (produkt,cena,ilosc, wartosc)
        historia.append(historia_zakup)

        continue


    if wybor == "sprzedaz":
        print('/jestesmy w sprzedaz/')


        print('podaj nazwe produktu do sprzedania:')
        produkt = str(input())

#  poprawic sprawdzenie czy jest w magazynie (not in magazyn) !!!!

# if produkt not in magazyn:
# print('Brak produktu w magazynie!')
# continue

        print('podaj cene sprzedazy produktu:')
        cena = int(input())
        if cena <= 0:
            print('Zla cena!')
            continue

        print('podaj ilosc sztuk do sprzedania:')
        ilosc = int(input())
        if ilosc <= 0:
            print('Zła ilość!')
            continue

        if ilosc < ilosc in magazyn:
            print('Brak takiej ilosci w magazynie')
            continue

        wartosc_produkt = cena * ilosc
        stan_konta += cena * ilosc
        magazyn[produkt] -= ilosc

# do zrobienia: wyrzucic produkt z magazynu gdy stan produktu = zero ????

        historia_sprzedaz = (produkt,cena,ilosc, wartosc)
        historia.append(historia_sprzedaz)

# printa ponizej poprawic
#        print(f,"Sprzedano",{ilosc}, {produkt}, "o wartosci:", {wartosc_produkt})
        continue

    if wybor == "konto":
        print('/jestesmy w  konto/')
        print (f'aktualny stan konta to: {stan_konta}')
        continue

    if wybor == "magazyn":
        print('/jestesmy w  magazyn/')

# zrobic: w nowych liniach, bez nawiasów

        print (f'aktualny stan magazynu to:\n {magazyn}')
        continue

# program wypisuje stany magazynowe dla podanych produktów, w formacie:
# <id produktu>: <stan> w nowych liniach i kończy działanie:

    if wybor == "przeglad":
        print('/jestesmy w  przeglad/')
        print(historia)
        continue

    if wybor == "stop":
        print('jestesmy w stop')
        print('koniec')
        break

"""

sad = sys.argv[1]        # argv pod saldo
spr = sys.argv[1]        # argv pod sprzedaz
zak = sys.argv[1]        # argv pod zakup

kon= sys.argv[1]        # argv pod konto
len(sys.argv))
for x in range

mga = sys.argv[1]        # argv pod magazyn
prz = sys.argv[1]        # argv pod przeglad


"""
