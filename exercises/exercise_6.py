a = int(input())
b = int(input())

isDivisible = 'Yes' * (a % b == 0) or 'No'

print(isDivisible)