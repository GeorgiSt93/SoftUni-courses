chicken_menu = int(input())
fish_menu = int(input())
vegg_menu = int(input())

CHICKEN_MENU_P = 10.35
FISH_MENU_P = 12.40
VEGG_MENU_P = 8.15
DELIVERY = 2.50

order_price = (chicken_menu * CHICKEN_MENU_P) +\
              (fish_menu * FISH_MENU_P) +\
              (vegg_menu * VEGG_MENU_P)

desert = order_price * 0.20
total_price = order_price + desert + DELIVERY

print(total_price)

