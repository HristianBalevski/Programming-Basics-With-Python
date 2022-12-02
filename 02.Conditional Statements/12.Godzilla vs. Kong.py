budjet = float(input())
people_cnt = int(input())
price_for_clothes_1_person = float(input())

decor = budjet * 0.10
price_for_clothes = people_cnt * price_for_clothes_1_person
total_money = price_for_clothes + decor

if people_cnt > 150:

    discount = price_for_clothes * 0.10
    price_for_clothes -= discount
    total_money = price_for_clothes + decor

if total_money > budjet:
    needed_money = total_money - budjet
    print('Not enough money!')
    print(f'Wingard needs {needed_money:.2f} leva more.')
else:
    money_left = budjet - total_money
    print('Action!')
    print(f'Wingard starts filming with {money_left:.2f} leva left.')
