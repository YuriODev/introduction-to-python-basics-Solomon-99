# Exercise 4
# Your solution comes here

number = input('Enter a 4-digit number: ')

if number[0:2] == number[::-2]:
      print(1)
else:
      print(0)