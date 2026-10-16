a = 0
b = 0
while True:
    c = float(input())
    if c == 0: break
    a += c
    b += 1

print(f"кількість = {b}, сума = {a}, середнє = {a/b}")