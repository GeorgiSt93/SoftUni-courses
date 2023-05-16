days_stay = int(input())
type_room = str(input())
grade = str(input())

price = 0

ONE_P = 18.00
APARTMENT = 25.00
P_APART = 35.00

if 1 <= days_stay < 10:
    if type_room == 'room for one person':
        price = (days_stay - 1) * ONE_P
    elif type_room == 'apartment':
        price = ((days_stay - 1) * APARTMENT) * 0.70
    elif type_room == 'president apartment':
        price = ((days_stay - 1) * P_APART) * 0.90

elif 10 <= days_stay < 15:
    if type_room == 'room for one person':
        price = (days_stay - 1) * ONE_P
    elif type_room == 'apartment':
        price = ((days_stay - 1) * APARTMENT) * 0.65
    elif type_room == 'president apartment':
        price = ((days_stay - 1) * P_APART) * 0.85

elif days_stay >= 15:
    if type_room == 'room for one person':
        price = (days_stay - 1) * ONE_P
    elif type_room == 'apartment':
        price = ((days_stay - 1) * APARTMENT) * 0.50
    elif type_room == 'president apartment':
        price = ((days_stay - 1) * P_APART) * 0.80

if grade == 'positive':
    print(f'{price * 1.25:.2f} ')
elif grade == 'negative':
    print(f'{price * 0.90:.2f}')


