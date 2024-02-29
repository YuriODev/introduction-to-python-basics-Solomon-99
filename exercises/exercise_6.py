a = int(input())
b = int(input())

divisible = 'Yes' * (a % b == 0) or 'No'

print(divisible)