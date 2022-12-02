nylon = int(input())
paint = int(input())
water = int(input())
hours = int(input())

nylon = (nylon + 2) * 1.50
added_paint = paint * 0.1
paint = paint + added_paint
paint = paint * 14.50
water = water * 5
bags = 0.40

all_materials = nylon + paint + bags + water
price_per_hour = all_materials * 0.30
hours = hours * price_per_hour

total_money = nylon + paint + water + bags + hours

print(total_money)
