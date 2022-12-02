n = int(input())
r1 = 0
r2 = 0
r3 = 0
r4 = 0
r5 = 0

for i in range(0, n):
    current_number = int(input())

    if current_number < 200:
        r1 += 1
    elif current_number <= 399:
        r2 += 1
    elif current_number <= 599:
        r3 += 1
    elif current_number <= 799:
        r4 += 1
    else:
        r5 += 1

p1 = (r1 / n) * 100
print(f'{p1:.2f}%')
p2 = (r2 / n) * 100
print(f'{p2:.2f}%')
p3 = (r3 / n) * 100
print(f'{p3:.2f}%')
p4 = (r4 / n) * 100
print(f'{p4:.2f}%')
p5 = (r5 / n) * 100
print(f'{p5:.2f}%')
