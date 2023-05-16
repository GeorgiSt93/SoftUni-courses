trip = float(input())

puzzles = int(input())
dolls = int(input())
teddies = int(input())
minions = int(input())
lorries = int(input())

PUZZLE_PRICE = 2.60
DOLL_PRICE = 3
TEDDIE = 4.10
MINION = 8.20
LORRY = 2

toy_price = (puzzles * PUZZLE_PRICE) + \
            (dolls * DOLL_PRICE) + (teddies * TEDDIE) + \
            (minions * MINION) + (lorries * LORRY)
toy_amount = puzzles + dolls + teddies + minions + lorries

if toy_amount >= 50:
    toy_price *= 0.75

toy_price *= 0.90

if toy_price >= trip:
    print(f'Yes! {toy_price - trip:.2f} lv left.')
else:
    print(f'Not enough money! {trip - toy_price:.2f} lv needed.')




