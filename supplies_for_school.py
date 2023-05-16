pen_packs = int(input())
marker_packs = int(input())
detergent_l = int(input())
discount = int(input()) / 100

PEN_PRICE = 5.80
MARKER_PRICE = 7.20
DETERGENT_PRICE = 1.20

price_nd = (pen_packs * PEN_PRICE) + \
           (marker_packs * MARKER_PRICE) + \
           (detergent_l * DETERGENT_PRICE)
total = price_nd - price_nd * discount

print(total)

