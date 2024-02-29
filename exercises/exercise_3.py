# Exercise 3
# Your solution comes here

def calc_Time(n):
      hours = (n // 3600) % 24
      minutes = (n//60) % 60
      seconds = n % 60
      return f'{hours}:{minutes:02d}:{seconds:02d}'

print(calc_Time(int(input())))