pages = int(input())
pages_per_hour = int(input())
days_to_finish_the_book = int(input())

total_time_needed = pages // pages_per_hour
pages_a_day = total_time_needed // days_to_finish_the_book

print(pages_a_day)

