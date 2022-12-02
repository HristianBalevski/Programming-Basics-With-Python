tax_per_year = int(input())

sneakers = tax_per_year - (tax_per_year * 0.40)
equipment = sneakers - (sneakers * 0.20)
ball = equipment * 0.25
accessories = ball * 0.20

needed_money = tax_per_year + sneakers + equipment + ball + accessories

print(needed_money)
