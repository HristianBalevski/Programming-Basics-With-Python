budget = float(input())
season = input()
destination = ''
sleeping = ''
money = 0

if budget <= 100:
    destination = 'Bulgaria'
    if season == 'summer':
        money = budget * 0.30
        sleeping = 'Camp'
    elif season == 'winter':
        money = budget * 0.70
        sleeping = 'Hotel'
elif budget <= 1000:
    destination = 'Balkans'
    if season == 'summer':
        money = budget * 0.40
        sleeping = 'Camp'
    elif season == 'winter':
        money = budget * 0.80
        sleeping = 'Hotel'
elif budget > 1000:
    destination = 'Europe'
    money = budget * 0.90
    sleeping = 'Hotel'
print(f'Somewhere in {destination}')
print(f'{sleeping} - {money:.2f}')
