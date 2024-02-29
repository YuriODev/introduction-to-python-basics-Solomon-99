s = int(input())

bills500 = s // 500
s %= 500

bills100 = s // 100
s %= 100

bills10 = s // 10
s %= 10

bills5 = s // 5
s %= 5

bills1 = s

print(f"{bills500} (500), {bills100} (100), {bills10} (10), {bills5} (5), {bills1} (1)")