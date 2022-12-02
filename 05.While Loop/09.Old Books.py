name_of_book = input()
current_book = input()
counter = 0

while current_book != 'No More Books':

    if current_book == name_of_book:
        print(f'You checked {counter} books and found it.')
        break
    counter += 1
    current_book = input()
else:
    print('The book you search is not here!')
    print(f'You checked {counter} books.')
