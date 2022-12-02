lily_age = int(input())
washer_price = float(input())
single_toy_price = int(input())
toys_cnt = 0
total_money_save = 0

for age in range(1, lily_age + 1):

    if age % 2 != 0:
        toys_cnt += 1
    else:
        money_given = (age * 5) - 1
        total_money_save += money_given

toys_money = toys_cnt * single_toy_price
total_money_save += toys_money

if total_money_save >= washer_price:
    money_left = total_money_save - washer_price
    print(f'Yes! {money_left:.2f}')
else:
    needed_money = washer_price - total_money_save
    print(f'No! {needed_money:.2f}')
