number_of_students = int(input())
v_good, good, average, poor = 0, 0, 0, 0

sum_grades = 0

for count in range(number_of_students):
    grade = float(input())

    if grade >= 5.00:
        v_good += 1
    elif 4 <= grade <= 4.99:
        good += 1
    elif 3 <= grade <= 3.99:
        average += 1
    elif grade < 3:
        poor += 1

    sum_grades += grade

print(f'Top students: {v_good / number_of_students * 100:.2f}%')
print(f'Between 4.00 and 4.99: {good / number_of_students * 100:.2f}%')
print(f'Between 3.00 and 3.99: {average / number_of_students * 100:.2f}%')
print(f'Fail: {poor / number_of_students * 100:.2f}%')
print(f'Average: {sum_grades / number_of_students:.2f}')
