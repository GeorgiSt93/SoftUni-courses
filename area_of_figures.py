from math import pi

shape = input()
area = 0

if shape == 'square':
    a = float(input())
    area = a * a
    print(f'{area:.3f}')
elif shape == 'rectangle':
    a = float(input())
    b = float(input())
    area = a * b
    print(f'{area:.3f}')
elif shape == 'circle':
    r = float(input())
    area = pi * (r ** 2)
    print(f'{area:.3f}')
elif shape == 'triangle':
    a = float(input())
    b = float(input())
    area = 1/2 * a * b
    print(f'{area:.3f}')



