deposit = float(input())
time_of_deposit = int(input())
percent = float(input()) /100

suma = deposit + time_of_deposit * ((deposit * percent ) / 12)

print(suma)
