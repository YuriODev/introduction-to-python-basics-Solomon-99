# Exercise 1
# Your solution comes here

# number = input('Enter a 5 digit number: ')
# # print(number)

# new_number = str(int(number[0])+int(number[2])+int(number[4])) + str(int(number[1])+int(number[3]))

# print(new_number)

number = int(input('Enter a 5 digit number: '))

num1 = number // 10000
num2 = (number // 100) % 10
num3 = number % 10
num4 = (number // 1000) % 10
num5 = (number // 10) % 10

first_Part = num1 + num3 + num5
second_Part = num2 + num4

print(str(first_Part) + str(second_Part))