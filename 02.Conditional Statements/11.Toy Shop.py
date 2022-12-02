price_holiday = float(input())
puzzles = int(input())
speaking_toys = int(input())
teddy_bears = int(input())
minions = int(input())
trucks = int(input())

total_toys_amount = puzzles + speaking_toys + teddy_bears + minions + trucks

puzzle_price = 2.60
speaking_toy_price = 3
teddy_bear_price = 4.10
minion_price = 8.20
truck_price = 2

total_price = puzzles * puzzle_price + speaking_toys * speaking_toy_price\
    + teddy_bears * teddy_bear_price + minions * minion_price + trucks * truck_price

if total_toys_amount >= 50:
    total_price = total_price * .75

rent = total_price * .10
profits = total_price - rent


if profits >= price_holiday:
    money_left = profits - price_holiday
    print(f"Yes! {money_left:.2f} lv left.")
else:
    money_left = price_holiday - profits
    print(f"Not enough money! {money_left:.2f} lv needed.")
