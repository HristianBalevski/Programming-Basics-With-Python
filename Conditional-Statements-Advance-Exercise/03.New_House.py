type_of_flower = input()
flower_cnt = int(input())
budget = int(input())
discount = 0
price_up = 0
final_price = 0
Roses = 0
Dahlias = 0
Tulips = 0
Narcissus = 0
Gladiolus = 0
roses_price = flower_cnt * 5
dahlias_price = flower_cnt * 3.80
tulips_price = flower_cnt * 2.80
narcissus_price = flower_cnt * 3
gladiolus_price = flower_cnt * 2.50

if type_of_flower == 'Roses':
    if flower_cnt > 80:
        discount = roses_price * 0.10
        final_price = roses_price - discount
    else:
        final_price = roses_price
if type_of_flower == 'Dahlias':
    if flower_cnt > 90:
        discount = dahlias_price * 0.15
        final_price = dahlias_price - discount
    else:
        final_price = dahlias_price
if type_of_flower == 'Tulips':
    if flower_cnt > 80:
        discount = tulips_price * 0.15
        final_price = tulips_price - discount
    else:
        final_price = tulips_price
if type_of_flower == 'Narcissus':
    if flower_cnt < 120:
        price_up = narcissus_price * 0.15
        final_price = narcissus_price + price_up
    else:
        final_price = narcissus_price
if type_of_flower == 'Gladiolus':
    if flower_cnt < 80:
        price_up = gladiolus_price * 0.20
        final_price = gladiolus_price + price_up
    else:
        final_price = gladiolus_price
if budget >= final_price:
    money_left = budget - final_price
    print(f'Hey, you have a great garden with {flower_cnt} {type_of_flower} and {money_left:.2f} leva left.')
else:
    needed_money = final_price - budget
    print(f'Not enough money, you need {needed_money:.2f} leva more.')
