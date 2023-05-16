CPU_price_USD = float(input())
GPU_price_USD = float(input())
RAM_price_USD = float(input())
RAM_count = int(input())
discount = float(input())

lv_to_usd = 1.57

cpu_in_lv = CPU_price_USD * lv_to_usd
gpu_in_lv = GPU_price_USD * lv_to_usd
ram_in_lv = RAM_price_USD * lv_to_usd
ram_total_lv = ram_in_lv * RAM_count

cpu_w_dc = cpu_in_lv - (cpu_in_lv * discount)
gpu_w_dc = gpu_in_lv - (gpu_in_lv * discount)

total_price = cpu_w_dc + gpu_w_dc + ram_total_lv

print(f'Money needed - {total_price:.2f} leva.')
