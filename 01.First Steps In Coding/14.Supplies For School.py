pen_cnt = int(input())
markers_cnt = int(input())
mr_proper = int(input())
discount = int(input()) / 100

pen_price = pen_cnt * 5.80
marker_price = markers_cnt * 7.20
mrprper_price = mr_proper * 1.20

full_price = pen_price + marker_price + mrprper_price
discount = full_price * discount
needed_money = full_price - discount

print(needed_money)
