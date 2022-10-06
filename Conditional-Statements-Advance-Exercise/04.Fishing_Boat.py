budget = int(input())
season = input()
anglers_cnt = int(input())

rent_for_boat = 0
discount = 0
discount2 = 0

if season == 'Spring':
    rent_for_boat = 3000
    if anglers_cnt <= 6:
        discount = rent_for_boat * 0.10
    elif 7 <= anglers_cnt <= 11:
        discount = rent_for_boat * 0.15
    elif anglers_cnt >= 12:
        discount = rent_for_boat * 0.25
elif season == 'Summer' or season == 'Autumn':
    rent_for_boat = 4200
    if anglers_cnt <= 6:
        discount = rent_for_boat * 0.10
    elif 7 <= anglers_cnt <= 11:
        discount = rent_for_boat * 0.15
    elif anglers_cnt >= 12:
        discount = rent_for_boat * 0.25
elif season == 'Winter':
    rent_for_boat = 2600
    if anglers_cnt <= 6:
        discount = rent_for_boat * 0.10
    elif 7 <= anglers_cnt <= 11:
        discount = rent_for_boat * 0.15
    elif anglers_cnt >= 12:
        discount = rent_for_boat * 0.25
money_needed = rent_for_boat - discount
if season == 'Spring' or season == 'Summer' or season == 'Winter':
    if anglers_cnt % 2 == 0:
        discount2 = money_needed * 0.05
money_needed = (rent_for_boat - discount) - discount2
if budget >= money_needed:
    money_left = budget - money_needed
    print(f'Yes! You have {money_left:.2f} leva left.')
else:
    not_enough_money = money_needed - budget
    print(f'Not enough money! You need {not_enough_money:.2f} leva.')
