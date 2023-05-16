budget = float(input())
season = str(input())

price = 0
place = None
destination = None

if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        price = budget * 0.30
        place = "Camp"
    elif season == "winter":
        price = budget * 0.70
        place = "Hotel"

elif 100 < budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        price = budget * 0.40
        place = "Camp"
    elif season == "winter":
        price = budget * 0.80
        place = "Hotel"

elif budget > 1000:
    destination = "Europe"
    if season == "summer":
        price = budget * 0.90
        place = "Hotel"
    elif season == "winter":
        price = budget * 0.90
        place = "Hotel"

print(f'Somewhere in {destination}')
print(f'{place} - {price:.2f}')

