import sys
action = ["saldo", "purchase", "sale", "konto", "magazyn", "overview", "stop"]
saldo = 0            # initial balance
sale = 0             # initial sale
purchase = 0         # purchase
magazyn = {}         # dict
history = []         # all operations
comment = True       # comment
value = 0            # balance value entered
current_balance = 0  # cash
price = 0            # initial price
value_product = 0    # price * quantity

while True:
    choice = str(input().strip())    # strip - returns pure string
    if choice not in action:
        print(f'Bad choice. {choice} Try again!')
        continue
    if choice == "saldo":
        value = int(input())
        if value == 0:
            print('Donate a bit more ;)')
            continue
        if current_balance + value <= 0:
            print('Wrong amount, no payout possible!')
            continue
        comment = str(input())
        if comment == "stop":
            print("Transaction canceled!")
            continue
        current_balance += value
        history_saldo = (choice, value, comment)
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
        quantity = int(input())
        if quantity <= 0 or quantity * price > current_balance:
            print('No funds to purchase')
            break
        current_balance -= price * quantity
        value_product = price * quantity
        if product in magazyn:
            magazyn[product] += quantity
        else:
            magazyn[product] = quantity
        history_purchase = (choice, product, price, quantity)
        history.append(history_purchase)
        continue
    if choice == "sale":
        product = str(input())
        if product not in magazyn:
            print('No product in stock!')
            continue
        price = int(input())
        if price <= 0:
            print('Bad price!')
            continue
        quantity = int(input())
        if quantity <= 0:
            print('Bad quantity!')
            continue
        if magazyn[product] < quantity:
            print('No such quantity in stock')
            continue
        value_product = price * quantity
        current_balance += price * quantity
        magazyn[product] -= quantity
        history_sale = (choice, product, price, quantity)
        history.append(history_sale)
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
    value = int(sys.argv[2])
    comment = sys.argv[3]
    current_balance += value
    history_saldo = (choice, value, comment)
    history.append(history_saldo)

if sys.argv[1] == "purchase":
    product = str(sys.argv[2])
    price = int(sys.argv[3])
    quantity = int(sys.argv[4])
    current_balance -= price * quantity
    value_product = price * quantity
    magazyn[product] += quantity
    history_purchase = (choice, product, price, quantity)
    history.append(history_purchase)

if sys.argv[1] == "sale":
    product = str(sys.argv[2])
    price = int(sys.argv[3])
    quantity = int(sys.argv[4])
    value_product = price * quantity
    current_balance += price * quantity
    magazyn[product] -= quantity
    history_sale = (choice, product, price, quantity)
    history.append(history_sale)

if sys.argv[1] in ("saldo", "purchase", "sale"):
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
