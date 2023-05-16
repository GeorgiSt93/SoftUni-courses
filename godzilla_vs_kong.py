production_budget = float(input())
extras = int(input())
costume_price_per_extra = float(input())

props = production_budget * 0.10

if extras > 150:
    costume_price_per_extra *= 0.90

production_price = props + extras * costume_price_per_extra

if production_price > production_budget:
    print("Not enough money!")
    print(f"Wingard needs {production_price - production_budget:.2f} leva more.")
elif production_price <= production_budget:
    print("Action!")
    print(f"Wingard starts filming with {production_budget - production_price:.2f} leva left.")

