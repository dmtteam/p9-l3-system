import sys
akcja= ["saldo", "zakup", "sprzedaz", "konto", "magazyn", "przeglad", "stop"]
saldo = 0
sprzedaz = 0
zakup = 0
magazyn = {}         # slownik
historia = []        # lista wyswietlana w przeglad
komentarz = True     # przydatne do anulowania transakcji na poziomie komentarza w saldzie
wartosc = 0          # poczatkowe saldo na koncie
stan_konta = 0       # tu przechowuje aktualne saldo
cena = 0             # def ceny produktu
wartosc_produkt = 0  # wartosc kupionego produktu (cena * ilosc)

while True:
    wybor = str(input().strip())    # strip - zwraca czysty ciag znakow
    if wybor not in akcja:
        print(f'Zły wybor. {wybor} Jeszcze raz')
        continue
    if wybor == "saldo":
        wartosc = int(input())
        if wartosc == 0:
            print('Wpłać ciut więcej ;)')
            continue
        if stan_konta + wartosc <= 0:
            print('Zla kwota, brak mozliwosci wyplaty')
            continue
        komentarz = str(input())
        if komentarz == "stop":
            print("Transakcja anulowana")
            continue
        stan_konta += wartosc
        historia_saldo = (wybor,wartosc,komentarz)
        historia.append(historia_saldo)
        continue
    if wybor == "zakup":
        produkt = str(input())
        cena = int(input())
        if cena <= 0:
            print('Zla cena!')
            continue
        if cena > stan_konta:
            print('Brak srodkow na zakup')
            break
        ilosc = int(input())
        if ilosc <= 0 or ilosc * cena > stan_konta:
            print('Brak srodkow na zakup')
            break
        stan_konta -= cena * ilosc
        wartosc_produkt = cena * ilosc
        if produkt in magazyn:
            magazyn[produkt] += ilosc
        else:
            magazyn[produkt] = ilosc
        historia_zakup = (wybor,produkt,cena,ilosc)
        historia.append(historia_zakup)
        continue
    if wybor == "sprzedaz":
        produkt = str(input())
        if produkt not in magazyn:
            print('Brak produktu w magazynie!')
            continue
        cena = int(input())
        if cena <= 0:
            print('Zla cena!')
            continue
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
        continue
    if wybor == "konto":
        print (f'aktualny stan konta to: {stan_konta}')
        continue
    if wybor == "magazyn":
        for wiersz in magazyn:
            print(wiersz)
        print("stop")
        continue
    if wybor == "przeglad":
        for ile in historia:
            print(ile)
        continue
    if wybor == "stop":
        break

# argv
wybor = sys.argv[1]
if sys.argv[1] == "saldo":
    wartosc = int(sys.argv[2])
    komentarz = sys.argv[3]
    stan_konta += wartosc
    historia_saldo = (wybor, wartosc, komentarz)
    historia.append(historia_saldo)

if sys.argv[1] == "zakup":
    produkt = str(sys.argv[2])
    cena = int(sys.argv[3])
    ilosc = int(sys.argv[4])
    stan_konta -= cena * ilosc
    wartosc_produkt = cena * ilosc
    magazyn[produkt] += ilosc
    historia_zakup = (wybor,produkt,cena,ilosc)
    historia.append(historia_zakup)

if sys.argv[1] == "sprzedaz":
    produkt = str(sys.argv[2])
    cena = int(sys.argv[3])
    ilosc = int(sys.argv[4])
    wartosc_produkt = cena * ilosc
    stan_konta += cena * ilosc
    magazyn[produkt] -= ilosc
    historia_sprzedaz = (wybor,produkt,cena,ilosc)
    historia.append(historia_sprzedaz)

if sys.argv[1] in ("saldo", "zakup", "sprzedaz"):
    for wiersz in historia:
        for element in wiersz:
            print(element)
    print("stop")

if sys.argv[1] == "konto":
    print(stan_konta)

if sys.argv[1] == "magazyn":
    for produkt in sys.argv[2:]:
        if produkt not in magazyn:
            stan_magazyn = 0
        else:
            stan_magazyn = magazyn[produkt]
        print(f'{produkt} : {stan_magazyn}')

if sys.argv[1] == "przeglad":
    for wiersz in historia:
        for element in wiersz:
            print(element)
    print("stop")

"""
elif sys.argv[1] =="przeglad":
    numerowana_baza = enumerate(rejestr_zdarzen)
    for index, aktywnosc in enumerate(rejestr_zdarzen[int(sys.argv[2]):int(sys.argv[3])]):
        print(aktywnosc)"""
