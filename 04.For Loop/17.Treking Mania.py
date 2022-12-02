groups_quantity = int(input())

mus = 0
mon = 0
kili = 0
k2 = 0
everest = 0

for groups in range(1, groups_quantity + 1):
    people_quantity = int(input())
    
    if people_quantity <= 5:
        mus += people_quantity
        
    elif 6 <= people_quantity <= 12:
        mon += people_quantity
        
    elif 13 <= people_quantity <= 25:
        kili += people_quantity
        
    elif 26 <= people_quantity <= 40:
        k2 += people_quantity
    else:
        everest += people_quantity
        
total_people = mus + mon + kili + k2 + everest
mus = (mus / total_people) * 100
mon = (mon / total_people) * 100
kili = (kili / total_people) * 100
k2 = (k2 / total_people) * 100
everest = (everest / total_people) * 100

print(f'{mus:.2f}%')
print(f'{mon:.2f}%')
print(f'{kili:.2f}%')
print(f'{k2:.2f}%')
print(f'{everest:.2f}%')
