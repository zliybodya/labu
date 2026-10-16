cina = float(input("Ведіть ціну "))
kilkist = int(input("Ведіть кількість "))
znyrzka = float(input("Ведіть знижку "))

wse = cina*kilkist
sumaZnyrzky = wse*znyrzka/100
wseZiZnyrzkoju = wse-sumaZnyrzky

print(f"ціна без знижки складає {wse:.2f}")
print(f"знижка складає {sumaZnyrzky:.2f}")
print(f"ціна зі знижкою слк {wseZiZnyrzkoju:.2f}")