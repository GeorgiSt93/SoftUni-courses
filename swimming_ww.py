from math import floor

record_sec = float(input())
distance = float(input())
sec_per_meter = float(input())

time_swimming = distance * sec_per_meter
water_resistance = floor(distance / 15) * 12.5
total_time = time_swimming + water_resistance

if total_time < record_sec:
    print(f'Yes, he succeeded! The new world record is {total_time:.2f} seconds.')
else:
    print(f'No, he failed! He was {total_time - record_sec:.2f} seconds slower.')

