people = int(input())
season = str(input())

price_per_person = 0

if season == "spring":
    if people <= 5:
        price_per_person = 50
    elif people > 5:
        price_per_person = 48

elif season == "summer":
    if people <= 5:
        price_per_person = 48.50 * 0.85
    elif people > 5:
        price_per_person = 45 * 0.85

elif season == "autumn":
    if people <= 5:
        price_per_person = 60
    elif people > 5:
        price_per_person = 49.50

elif season == "winter":
    if people <= 5:
        price_per_person = 86 * 1.08
    elif people > 5:
        price_per_person = 85 * 1.08

print(f'{people * price_per_person:.2f} leva.')
