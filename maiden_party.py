party_price = float(input())
love_letters = int(input())
roses = int(input())
keychains = int(input())
images = int(input())
surprises = int(input())

LOVE_LETTER_PRICE = 0.60
ROSE_PRICE = 7.20
KEYCHAIN = 3.60
IMAGE = 18.20
SURPRISE = 22

price = love_letters * LOVE_LETTER_PRICE + roses * ROSE_PRICE \
        + keychains * KEYCHAIN + images * IMAGE + surprises * SURPRISE

sold_items = love_letters + roses + keychains + images + surprises

if sold_items > 25:
    price *= .65

hosting = price * 0.10

total_price = price - hosting

if total_price > party_price:
    print(f'Yes! {total_price - party_price:.2f} lv left.')
else:
    print(f'Not enough money! {party_price - total_price:.2f} lv needed.')
