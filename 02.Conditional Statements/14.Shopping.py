budget = float(input())
cards_cnt = int(input())
processors_cnt = int(input())
ram_cnt = int(input())

cards_price = cards_cnt * 250
processors_price = (cards_price * 0.35) * processors_cnt
ram_price = (cards_price * 0.10) * ram_cnt

spent_money = cards_price + processors_price + ram_price

if cards_cnt > processors_cnt:
    discount = spent_money * 0.15
    spent_money = spent_money - discount

if budget >= spent_money:
    money_left = budget - spent_money
    print(f'You have {money_left:.2f} leva left!')
else:
    needed_money = spent_money - budget
    print(f'Not enough money! You need {needed_money:.2f} leva more!')
