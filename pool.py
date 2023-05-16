from math import ceil

people = int(input())
fee = float(input())
sun_league_price = float(input())
umbrella_price = float(input())

entry_fee = people * fee
sun_league = ceil(people * 0.75) * sun_league_price
umbrellas = ceil(people * 0.50) * umbrella_price

total_fee = entry_fee + sun_league + umbrellas

print(f'{total_fee:.2f} lv.')
