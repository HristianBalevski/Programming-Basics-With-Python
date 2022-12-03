jury_quantity = int(input())

current_presentation = []
all_presentation = []

while True:
    presentation = input()
    if presentation == 'Finish':
        break

    for i in range(jury_quantity):
        grades = float(input())
        current_presentation.append(grades)
        all_presentation.append(grades)

    average_grade = sum(current_presentation) / len(current_presentation)
    print(f"{presentation} - {average_grade:.2f}.")
    current_presentation.clear()

all_average_grades = sum(all_presentation) / len(all_presentation)
print(f"Student's final assessment is {all_average_grades:.2f}.")
