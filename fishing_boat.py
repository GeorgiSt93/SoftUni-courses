budget = int(input())
season = str(input())
fishermen = int(input())

ship_rent = 0

if season == "Spring":
    ship_rent = 3000
elif season == "Winter":
    ship_rent = 2600
else:
    ship_rent = 4200

if fishermen <= 6:
    ship_rent *= 0.90
elif 7 <= fishermen <= 11:
    ship_rent *= 0.85
elif fishermen > 12:
    ship_rent *= 0.75

if fishermen % 2 == 0 and season != "Autumn":
    ship_rent *= 0.95

if budget >= ship_rent:
    print(f'Yes! You have {budget - ship_rent:.2f} leva left.')
elif budget < ship_rent:
    print(f'Not enough money! You need {abs(ship_rent - budget):.2f} leva.')


