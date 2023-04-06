import sys
action = ["saldo", "purchase", "sprzedaz", "konto", "magazyn", "overview", "stop"]
saldo = 0            # balance
sprzedaz = 0         # sale
purchase = 0         # purchase
magazyn = {}         # dict
history = []         # all operations
comment = True       # comment
wartosc = 0          # initial balance
current_balance = 0  # cash
price = 0            # initial price
value_product = 0    # price * quantity

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
        if current_balance + wartosc <= 0:
            print('Wrong amount, no payout possible!')
            continue
        comment = str(input())
        if comment == "stop":
            print("Transaction canceled!")
            continue
        current_balance += wartosc
        history_saldo = (choice, wartosc, comment)
        history.append(history_saldo)
        continue
    if choice == "purchase":
        product = str(input())
        price = int(input())
        if price <= 0:
            print('Bad price!')
            continue
        if price > current_balance:
            print('No funds to purchase')
            break
        ilosc = int(input())
        if ilosc <= 0 or ilosc * price > current_balance:
            print('No funds to purchase')
            break
        current_balance -= price * ilosc
        value_product = price * ilosc
        if product in magazyn:
            magazyn[product] += ilosc
        else:
            magazyn[product] = ilosc
        history_purchase = (choice, product, price, ilosc)
        history.append(history_purchase)
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
        value_product = price * ilosc
        current_balance += price * ilosc
        magazyn[product] -= ilosc
        history_sprzedaz = (choice, product, price, ilosc)
        history.append(history_sprzedaz)
        continue
    if choice == "konto":
        print(f'Current account balance is: {current_balance}')
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
    current_balance += wartosc
    history_saldo = (choice, wartosc, comment)
    history.append(history_saldo)

if sys.argv[1] == "purchase":
    product = str(sys.argv[2])
    price = int(sys.argv[3])
    ilosc = int(sys.argv[4])
    current_balance -= price * ilosc
    value_product = price * ilosc
    magazyn[product] += ilosc
    history_purchase = (choice, product, price, ilosc)
    history.append(history_purchase)

if sys.argv[1] == "sprzedaz":
    product = str(sys.argv[2])
    price = int(sys.argv[3])
    ilosc = int(sys.argv[4])
    value_product = price * ilosc
    current_balance += price * ilosc
    magazyn[product] -= ilosc
    history_sprzedaz = (choice, product, price, ilosc)
    history.append(history_sprzedaz)

if sys.argv[1] in ("saldo", "purchase", "sprzedaz"):
    for line in history:
        for element in line:
            print(element)
    print("stop")

if sys.argv[1] == "konto":
    print(current_balance)

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
