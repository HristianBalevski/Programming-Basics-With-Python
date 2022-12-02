product = input()
city = input()
quantity = float(input())

if city == 'Sofia':
    if product == 'coffee':
        price = quantity * 0.50
        print(price)

    elif product == 'water':
        price = quantity * 0.80
        print(price)

    elif product == 'beer':
        price = quantity * 1.20
        print(price)

    elif product == 'sweets':
        price = quantity * 1.45
        print(price)

    elif product == 'peanuts':
        price = quantity * 1.60
        print(price)

if city == 'Plovdiv':
    if product == 'coffee':
        price = quantity * 0.40
        print(price)

    elif product == 'water':
        price = quantity * 0.70
        print(price)

    elif product == 'beer':
        price = quantity * 1.15
        print(price)

    elif product == 'sweets':
        price = quantity * 1.30
        print(price)

    elif product == 'peanuts':
        price = quantity * 1.50
        print(price)

if city == 'Varna':
    if product == 'coffee':
        price = quantity * 0.45
        print(price)

    elif product == 'water':
        price = quantity * 0.70
        print(price)

    elif product == 'beer':
        price = quantity * 1.10
        print(price)

    elif product == 'sweets':
        price = quantity * 1.35
        print(price)

    elif product == 'peanuts':
        price = quantity * 1.55
        print(price)
