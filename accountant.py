"""a) python accountant.py saldo <int wartosc> <str komentarz>
b) python accountant.py sprzedaż <str identyfikator produktu> <int cena> <int liczba sprzedanych>
c) python accountant.py zakup <str identyfikator produktu> <int cena> <int liczba zakupionych>
d) python accountant.py konto
e) python accountant.py magazyn <str identyfikator produktu 1> <str identyfikator produktu 2> <str identyfikator produktu 3> ...
f) python accountant.py przegląd"""

import sys

akcja= ["saldo", "zakup", "sprzedaz", "konto", "magazyn", "przeglad", "stop"]
saldo = 0
sprzedaz = 0
zakup = 0
konto = ""          # sprawdzic - po co to definiowac tu?
magazyn = {}        # slownik
historia = []       # lista wyswietlana w przeglad
stop = True         # konczy program, ewnetualnie dodac wszedzie
komentarz = True    # przydatne do anulowania transakcji na poziomie komentarza w saldzie
wartosc = 0         # poczatkowe saldo na koncie
stan_konta = 0      # tu przechowuje aktualne saldo
cena = 0            # def ceny produktu
wartosc_produkt = 0 # wartosc kupionego produktu (cena * ilosc)


while True:
# jak w 1 lini te 3 printy?
#print('#' * 87)
#print(f'Dostepne akcje: {akcja}\nCo wybierasz?')
#print('#' * 87)

    wybor = str(input("co wybierasz?"))
    if wybor not in akcja:
        print("Zły wybor. Jeszcze raz")
        continue

    if wybor == "saldo":
        wartosc = int(input('podaj wartosc transakcji'))

        if wartosc == 0:
            print('Wpłać ciut więcej ;)')
            continue

        if stan_konta + wartosc <= 0:
            print('Zla kwota, brak mozliwosci wyplaty')
            continue

        komentarz = str(input('podaj komentarz do transakcji - (STOP=anulowanie transakcji)'))
        if komentarz == "stop":
            print("Transakcja anulowana")
            continue

        stan_konta += wartosc
        historia_saldo = (wybor,wartosc,komentarz)
        historia.append(historia_saldo)

        print(f"Saldo: {wartosc} {komentarz}")
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

        print(f"Kupiono,{ilosc}, {produkt}, o wartosci:, {wartosc_produkt}")

        if produkt in magazyn:
            magazyn[produkt] += ilosc
        else:
            magazyn[produkt] = ilosc

        historia_zakup = (wybor,produkt,cena,ilosc)
        historia.append(historia_zakup)

        continue

    if wybor == "sprzedaz":
        print('podaj nazwe produktu do sprzedania:')
        produkt = str(input())

        if produkt not in magazyn:
            print('Brak produktu w magazynie!')
            continue
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
        if magazyn[produkt] < ilosc:
            print('Brak takiej ilosci w magazynie')
            continue

        wartosc_produkt = cena * ilosc
        stan_konta += cena * ilosc
        magazyn[produkt] -= ilosc

        historia_sprzedaz = (wybor,produkt,cena,ilosc)
        historia.append(historia_sprzedaz)

        print(f"Sprzedano,{ilosc}, {produkt}, o wartosci:, {wartosc_produkt}")
        continue

    if wybor == "konto":
        print (f'aktualny stan konta to: {stan_konta}')
        continue

    if wybor == "magazyn":

# stany magazynowe dla podanych produktów, w formacie:
# <id produktu>: <stan> w nowych liniach i kończy działanie:
        print (f'aktualny stan magazynu to:\n {magazyn}')


        continue



    if wybor == "przeglad":
        print('/jestesmy w  przeglad/')
#       print(historia)
        for ile in historia:
            print(ile)
# wypisuje wszystkie akcje zapisane pod indeksami w zakresie [od, do] (zakresy włącznie)


        continue



    if wybor == "stop":
        print('STOP')
        break

# argv

if sys.argv[1] == "saldo":
    wartosc = int(sys.argv[2])
    komentarz = sys.argv[3]
    stan_konta += wartosc
    historia_saldo = (wybor, wartosc, komentarz)
    historia.append(historia_saldo)

    print(f"{sys.argv[1]}\n{wartosc}\n{komentarz}")


if sys.argv[1] == "zakup":
    produkt = str(sys.argv[2])
    cena = int(sys.argv[3])
    ilosc = int(sys.argv[4])

    stan_konta -= cena * ilosc
    wartosc_produkt = cena * ilosc


    historia_zakup = (wybor,produkt,cena,ilosc)
    historia.append(historia_zakup)

    print(f"{sys.argv[1]}\n{produkt}\n{cena}\n{ilosc}")

if sys.argv[1] == "sprzedaz":
    produkt = str(sys.argv[2])
    cena = int(sys.argv[3])
    ilosc = int(sys.argv[4])

    wartosc_produkt = cena * ilosc
    stan_konta += cena * ilosc
    magazyn[produkt] -= ilosc

    historia_sprzedaz = (wybor,produkt,cena,ilosc)
    historia.append(historia_sprzedaz)

    print(f"{sys.argv[1]}\n {ilosc}\n{produkt},\n{cena}")

if sys.argv[1] == "konto":
    print(f'{sys.argv[1]}\n {stan_konta}')


if sys.argv[1] == "magazyn":
    print (f'{sys.argv[1]}\n {magazyn}')

# len(sys.argv))
# for x in range
# sys.argv[1] ==

if wybor == "przeglad":
    print(f'{sys.argv[1]}\n {historia}')
