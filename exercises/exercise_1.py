# Exercise 1
# Your solution comes here

number = int(input('Enter a 5 digit number: '))
number = list(str(number))
# print(number)

new_Number = str(int(number[0]) + int(number[2]) + int(number[4]))
new_Number = new_Number + str(int(number[1]) + int(number[3]))

print(new_Number)