stud = {}
with open("input.txt", "r") as t:
    a = t.read()
a = a.split(", ")
a = iter(a)
name = ""
bal = 0
for i in a:
    name, bal = i, int(next(a))
    stud[name] = bal
print(stud)
kilkist = len(stud)
ser = sum(stud.values())/kilkist
top_student = max(stud, key=stud.get)
loxu = []
for i in stud:
    if stud[i] < ser:
        loxu.append(f"{i}\n")
with open("output.txt", "w") as t:
    t.write(f"Students: {kilkist}\nAvarage: {ser}\nBest: {top_student}\nBelow avarage:\n")
    t.writelines(loxu)