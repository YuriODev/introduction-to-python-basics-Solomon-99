a = int(input())
b = int(input())
c = int(input())

min_value = min(a,b,c)
max_value = max(a,b,c)
mid_value = a + b + c - min_value - max_value
print(min_value)
print(mid_value)
print(max_value)