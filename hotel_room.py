month = str(input())
nights_spent = int(input())

studio_price = 0
app_price = 0

if month == "May" or month == "October":
    studio_price = 50
    app_price = 65

    if 7 < nights_spent <= 14:
        studio_price *= 0.95
    elif nights_spent > 14:
        studio_price *= 0.70
        app_price *= 0.90

elif month == "June" or month == "September":
    studio_price = 75.20
    app_price = 68.70

    if nights_spent > 14:
        studio_price *= 0.80
    elif nights_spent > 14:
        app_price *= 0.90

elif month == "July" or month == "August":
    studio_price = 76
    app_price = 77
    
    if nights_spent > 14:
        app_price *= 0.90

print(f'Apartment: {nights_spent * app_price:.2f} lv.')
print(f'Studio: {nights_spent * studio_price:.2f} lv.')
