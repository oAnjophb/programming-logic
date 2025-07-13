
qtyNumbers = int(input())

numbersInput = input().split()

if qtyNumbers != len(numbersInput):
    raise ValueError('invalid number of numbers')

number = list(map(int, numbersInput))

multiply_2 = 0
multiply_3 = 0
multiply_4 = 0
multiply_5 = 0

for num in number:
    if num % 2 == 0:
        multiply_2 += 1
    if num % 3 == 0:
        multiply_3 += 1
    if num % 4 == 0:
        multiply_4 += 1
    if num % 5 == 0:
        multiply_5 += 1

print(f'{multiply_2} Multiplo(s) de 2')
print(f'{multiply_3} Multiplo(s) de 3')
print(f'{multiply_4} Multiplo(s) de 4')
print(f'{multiply_5} Multiplo(s) de 5')
    