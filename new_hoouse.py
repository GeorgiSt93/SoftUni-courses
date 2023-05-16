type_of_flowers = str(input())
amount_of_flowers = int(input())
budget = int(input())

ROSES_PRICE = 5
DAHLIAS_PRICE = 3.80
TULIPS_PRICE = 2.80
NARCISSUS_PRICE = 3
GLADIOLUS_PRICE = 2.50

total_price = 0

if type_of_flowers == "Roses":
    total_price = amount_of_flowers * ROSES_PRICE

    if amount_of_flowers > 80:
        total_price *= 0.90

elif type_of_flowers == "Dahlias":
    total_price = amount_of_flowers * DAHLIAS_PRICE

    if amount_of_flowers > 90:
        total_price *= 0.85

elif type_of_flowers == "Tulips":
    total_price = amount_of_flowers * TULIPS_PRICE

    if amount_of_flowers > 80:
        total_price *= 0.85

elif type_of_flowers == "Narcissus":
    total_price = amount_of_flowers * NARCISSUS_PRICE

    if amount_of_flowers < 120:
        total_price *= 1.15

elif type_of_flowers == "Gladiolus":
    total_price = amount_of_flowers * GLADIOLUS_PRICE

    if amount_of_flowers < 80:
        total_price *= 1.20


if budget >= total_price:
    print(f'Hey, you have a great garden with {amount_of_flowers} {type_of_flowers} and \
{budget - total_price:.2f} leva left.')

else:
    print(f'Not enough money, you need {abs(total_price - budget):.2f} leva more.')
