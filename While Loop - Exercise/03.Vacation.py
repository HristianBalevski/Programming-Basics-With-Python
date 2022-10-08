needed_money_for_vacation = float(input())
available_money = float(input())
days_counter = 0
spend_days_counter = 0
saved_money = available_money

while True:
    action = input()
    amount = float(input())

    if action == 'spend':
        days_counter += 1
        spend_days_counter += 1
        if spend_days_counter == 5:
            print("You can't save the money.")
            print(days_counter)
            break
        if amount >= available_money:
            saved_money = 0
        else:
            saved_money -= amount

    if action == 'save':
        days_counter += 1
        spend_days_counter = 0
        saved_money += amount
        if saved_money >= needed_money_for_vacation:
            print(f'You saved the money for {days_counter} days.')
            break