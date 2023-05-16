budget = float(input())
gpus = int(input())
cpus = int(input())
ram_boards = int(input())

GPU_PRICE = 250
gpu_sold = gpus * GPU_PRICE

CPU_PRICE = gpu_sold * 0.35
RAM_PRICE = gpu_sold * 0.10

total = gpu_sold + (cpus * CPU_PRICE) + \
        (ram_boards * RAM_PRICE)

if gpus > cpus:
    total *= 0.85

if total <= budget:
    print(f'You have {budget - total:.2f} leva left!')
else:
    print(f'Not enough money! You need {total - budget:.2f} leva more!')
