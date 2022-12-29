import sys
akcja = ["saldo", "zakup", "sprzedaz", "konto", "magazyn", "przeglad", "stop"]
saldo = 0            # balance
sprzedaz = 0         # sale
zakup = 0            # purchase
magazyn = {}         # dict
historia = []        # all operations
komentarz = True     # comment
wartosc = 0          # initial balance
stan_konta = 0       # current balance
price = 0             # initial price
wartosc_produkt = 0  # price * quantity

while True:
    choice = str(input().strip())    # strip - returns pure string
    if choice not in akcja:
        print(f'Bad choice. {choice} Try again!')
        continue
    if choice == "saldo":
        wartosc = int(input())
        if wartosc == 0:
            print('Donate a bit more ;)')
            continue
        if stan_konta + wartosc <= 0:
            print('Wrong amount, no payout possible!')
            continue
        komentarz = str(input())
        if komentarz == "stop":
            print("Transaction canceled!")
            continue
        stan_konta += wartosc
        historia_saldo = (choice, wartosc, komentarz)
        historia.append(historia_saldo)
        continue
    if choice == "zakup":
        produkt = str(input())
        price = int(input())
        if price <= 0:
            print('Bad price!')
            continue
        if price > stan_konta:
            print('Brak srodkow na zakup')
            break
        ilosc = int(input())
        if ilosc <= 0 or ilosc * price > stan_konta:
            print('No funds to purchase')
            break
        stan_konta -= price * ilosc
        wartosc_produkt = price * ilosc
        if produkt in magazyn:
            magazyn[produkt] += ilosc
        else:
            magazyn[produkt] = ilosc
        historia_zakup = (choice, produkt, price, ilosc)
        historia.append(historia_zakup)
        continue
    if choice == "sprzedaz":
        produkt = str(input())
        if produkt not in magazyn:
            print('No product in stock!')
            continue
        price = int(input())
        if price <= 0:
            print('Bad price!')
            continue
        ilosc = int(input())
        if ilosc <= 0:
            print('Zła ilość!')
            continue
        if magazyn[produkt] < ilosc:
            print('No such quantity in stock')
            continue
        wartosc_produkt = price * ilosc
        stan_konta += price * ilosc
        magazyn[produkt] -= ilosc
        historia_sprzedaz = (choice, produkt, price, ilosc)
        historia.append(historia_sprzedaz)
        continue
    if choice == "konto":
        print(f'Current account balance is: {stan_konta}')
        continue
    if choice == "magazyn":
        for wiersz in magazyn:
            print(wiersz)
        print("stop")
        continue
    if choice == "przeglad":
        for ile in historia:
            print(ile)
        continue
    if choice == "stop":
        break

# argv
choice = sys.argv[1]
if sys.argv[1] == "saldo":
    wartosc = int(sys.argv[2])
    komentarz = sys.argv[3]
    stan_konta += wartosc
    historia_saldo = (choice, wartosc, komentarz)
    historia.append(historia_saldo)

if sys.argv[1] == "zakup":
    produkt = str(sys.argv[2])
    price = int(sys.argv[3])
    ilosc = int(sys.argv[4])
    stan_konta -= price * ilosc
    wartosc_produkt = price * ilosc
    magazyn[produkt] += ilosc
    historia_zakup = (choice, produkt, price, ilosc)
    historia.append(historia_zakup)

if sys.argv[1] == "sprzedaz":
    produkt = str(sys.argv[2])
    price = int(sys.argv[3])
    ilosc = int(sys.argv[4])
    wartosc_produkt = price * ilosc
    stan_konta += price * ilosc
    magazyn[produkt] -= ilosc
    historia_sprzedaz = (choice, produkt, price, ilosc)
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
