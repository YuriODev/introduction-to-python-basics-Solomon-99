a = int(input('Enter a number'))
b = int(input('Enter a number'))

isDivisible = 'Yes' * (a % b == 0) or 'No'

print(isDivisible)