deposited_sum = float(input())
deposit_term_in_month = int(input())
yearly_percent = float(input()) / 100

sum_deposit = deposited_sum + deposit_term_in_month * ((deposited_sum * yearly_percent) / 12 )

print(sum_deposit)

