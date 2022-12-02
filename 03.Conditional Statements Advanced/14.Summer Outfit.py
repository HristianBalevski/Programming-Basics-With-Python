degrees = int(input())
time_of_the_day = input()

Outfit = ''
Shoes = ''

if time_of_the_day == 'Morning':

    if 10 <= degrees <= 18:
        Outfit = 'Sweatshirt'
        Shoes = 'Sneakers'

    elif 18 < degrees <= 24:
        Outfit = 'Shirt'
        Shoes = 'Moccasins'

    elif degrees >= 25:
        Outfit = 'T-Shirt'
        Shoes = 'Sandals'

if time_of_the_day == 'Afternoon':

    if 10 <= degrees <= 18:
        Outfit = 'Shirt'
        Shoes = 'Moccasins'

    elif 18 < degrees <= 24:
        Outfit = 'T-Shirt'
        Shoes = 'Sandals'

    elif degrees >= 25:
        Outfit = 'Swim Suit'
        Shoes = 'Barefoot'

if time_of_the_day == 'Evening':

    if 10 <= degrees <= 18:
        Outfit = 'Shirt'
        Shoes = 'Moccasins'

    elif 18 < degrees <= 24:
        Outfit = 'Shirt'
        Shoes = 'Moccasins'

    elif degrees >= 25:
        Outfit = 'Shirt'
        Shoes = 'Moccasins'

print(f"It's {degrees} degrees, get your {Outfit} and {Shoes}.")
