# Exercise 5
# Your solution comes here

a = int(input())
b = int(input())

# print((a-b) > (b-a))

max_value = (a + b + abs(a - b)) // 2 #abs = magnitude

print(max_value)

# print(max(a, b))