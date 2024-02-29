n = int(input('Enter a number: '))

d1 = n // 1000
d2 = (n % 1000) // 100
d3 = (n % 100) // 10
d4 = n % 10

digit_Sum = d1 + d2 + d3 + d4
print(digit_Sum)