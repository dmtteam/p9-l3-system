import sys
action = ["saldo", "zakup", "sprzedaz", "konto", "magazyn", "overview", "stop"]
saldo = 0            # balance
sprzedaz = 0         # sale
zakup = 0            # purchase
magazyn = {}         # dict
history = []        # all operations
comment = True       # comment
wartosc = 0          # initial balance
stan_konta = 0       # current balance
price = 0             # initial price
wartosc_product = 0  # price * quantity

while True:
    choice = str(input().strip())    # strip - returns pure string
    if choice not in action:
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
        comment = str(input())
        if comment == "stop":
            print("Transaction canceled!")
            continue
        stan_konta += wartosc
        history_saldo = (choice, wartosc, comment)
        history.append(history_saldo)
        continue
    if choice == "zakup":
        product = str(input())
        price = int(input())
        if price <= 0:
            print('Bad price!')
            continue
        if price > stan_konta:
            print('No funds to purchase')
            break
        ilosc = int(input())
        if ilosc <= 0 or ilosc * price > stan_konta:
            print('No funds to purchase')
            break
        stan_konta -= price * ilosc
        wartosc_product = price * ilosc
        if product in magazyn:
            magazyn[product] += ilosc
        else:
            magazyn[product] = ilosc
        history_zakup = (choice, product, price, ilosc)
        history.append(history_zakup)
        continue
    if choice == "sprzedaz":
        product = str(input())
        if product not in magazyn:
            print('No product in stock!')
            continue
        price = int(input())
        if price <= 0:
            print('Bad price!')
            continue
        ilosc = int(input())
        if ilosc <= 0:
            print('Bad quantity!')
            continue
        if magazyn[product] < ilosc:
            print('No such quantity in stock')
            continue
        wartosc_product = price * ilosc
        stan_konta += price * ilosc
        magazyn[product] -= ilosc
        history_sprzedaz = (choice, product, price, ilosc)
        history.append(history_sprzedaz)
        continue
    if choice == "konto":
        print(f'Current account balance is: {stan_konta}')
        continue
    if choice == "magazyn":
        for line in magazyn:
            print(line)
        print("stop")
        continue
    if choice == "overview":
        for ile in history:
            print(ile)
        continue
    if choice == "stop":
        break

# argv
choice = sys.argv[1]
if sys.argv[1] == "saldo":
    wartosc = int(sys.argv[2])
    comment = sys.argv[3]
    stan_konta += wartosc
    history_saldo = (choice, wartosc, comment)
    history.append(history_saldo)

if sys.argv[1] == "zakup":
    product = str(sys.argv[2])
    price = int(sys.argv[3])
    ilosc = int(sys.argv[4])
    stan_konta -= price * ilosc
    wartosc_product = price * ilosc
    magazyn[product] += ilosc
    history_zakup = (choice, product, price, ilosc)
    history.append(history_zakup)

if sys.argv[1] == "sprzedaz":
    product = str(sys.argv[2])
    price = int(sys.argv[3])
    ilosc = int(sys.argv[4])
    wartosc_product = price * ilosc
    stan_konta += price * ilosc
    magazyn[product] -= ilosc
    history_sprzedaz = (choice, product, price, ilosc)
    history.append(history_sprzedaz)

if sys.argv[1] in ("saldo", "zakup", "sprzedaz"):
    for line in history:
        for element in line:
            print(element)
    print("stop")

if sys.argv[1] == "konto":
    print(stan_konta)

if sys.argv[1] == "magazyn":
    for product in sys.argv[2:]:
        if product not in magazyn:
            stan_magazyn = 0
        else:
            stan_magazyn = magazyn[product]
        print(f'{product} : {stan_magazyn}')

if sys.argv[1] == "overview":
    for line in history:
        for element in line:
            print(element)
    print("stop")
