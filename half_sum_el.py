from sys import maxsize

n = int(input())

max_num = -maxsize
sum_numbers = 0

for i in range(0, n):
    num = int(input())

    if num > max_num:
        max_num = num

sum_numbers += num

if max_num == sum_numbers - max_num:
    print("Yes")
    print(f"Sum = {sum_numbers}")
else:
    print("No")
    sum_numbers = sum_numbers - max_num
    print(f"Diff = {abs(max_num - sum_numbers)}")
