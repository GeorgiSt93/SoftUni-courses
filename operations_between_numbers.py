n1 = int(input())
n2 = int(input())
operator = input()

operation = 0

if operator == "+":
    operation = n1 + n2
    if operation % 2 == 0:
        print(f'{n1} {operator} {n2} = {operation} - even')
    elif operation % 2 != 0:
        print(f'{n1} {operator} {n2} = {operation} - odd')

if operator == "-":
    operation = n1 - n2
    if operation % 2 == 0:
        print(f'{n1} {operator} {n2} = {operation} - even')
    elif operation % 2 != 0:
        print(f'{n1} {operator} {n2} = {operation} - odd')

if operator == "*":
    operation = n1 * n2
    if operation % 2 == 0:
        print(f'{n1} {operator} {n2} = {operation} - even')
    elif operation % 2 != 0:
        print(f'{n1} {operator} {n2} = {operation} - odd')

if operator == "/":
    if n2 == 0:
        print(f'Cannot divide {n1} by zero')
    elif n2 != 0:
        operation = n1 / n2
        print(f'{n1} {operator} {n2} = {operation:.2f}')

if operator == "%":
    if n2 == 0:
        print(f'Cannot divide {n1} by zero')
    elif n2 != 0:
        operation = n1 % n2
        print(f'{n1} {operator} {n2} = {operation}')
