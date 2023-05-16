naylon = int(input())
paint = int(input())
thinner = int(input())
work_hours = int(input())

NAYLON_PRICE = 1.50
PAINT_PRICE = 14.50
THINNER_PRICE = 5.00
BAGS = 0.40

naylon += 2
paint += paint * 0.10

material_price = (naylon * NAYLON_PRICE) +\
                 (paint * PAINT_PRICE) +\
                 (thinner * THINNER_PRICE) + BAGS
price_per_hour = material_price * 0.30
total_price = material_price + (price_per_hour * work_hours)

print(total_price)
