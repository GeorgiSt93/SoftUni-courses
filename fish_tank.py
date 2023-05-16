length = int(input())
width = int(input())
height = int(input())
percentage_others = float(input())

vol = length * width * height
vol_in_litters = vol * 0.001
percentages = percentage_others / 100
litters_required = vol_in_litters * (1 - percentages)

print(litters_required)


