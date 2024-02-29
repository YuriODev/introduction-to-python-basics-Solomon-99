a = int(input())
b = int(input())

divisible = 'YES' * (a % b == 0) or 'NO'

print(divisible)