annual_fee = int(input())

SHOES = annual_fee - annual_fee * 0.40
JERSEY = SHOES - SHOES * 0.20
BALL = JERSEY * 1/4
ACCESORIES = BALL * 1/5

total_price = annual_fee +\
              SHOES + JERSEY +\
              BALL + ACCESORIES

print(total_price)