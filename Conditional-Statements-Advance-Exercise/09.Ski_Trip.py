days = int(input())
flat = input()
grade = input()
price = 0

if flat == 'room for one person':
    price = days * 18 - 18
if flat == 'apartment':
    price = days * 25 - 25
    if days < 10:
        discount = price * 0.30
        price = price - discount
    elif 10 <= days <= 15:
        price -= price * 0.35
    elif days > 15:
        discount = price * 0.50
        price = price - discount
if flat == 'president apartment':
    price = days * 35 - 35
    if days < 10:
        discount = price * 0.10
        price = price - discount
    elif 10 <= days <= 15:
        price -= price * 0.15
    elif days > 15:
        price -= price * 0.20
if grade == 'positive':
    price += price * 0.25
else:
    price -= price * 0.10
print(f'{price:.2f}')
