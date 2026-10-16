with open("input.txt", "r") as t:
    data = t.read()

if data == "":
    with open("output.txt", "w") as tt:
        tt.write("No data")
else:
    a = list(map(float, data.split(", ")))
    Max = max(a)
    min = min(a)
    kilkist = len(a)
    suma = sum(a)
    serednie = suma / kilkist

    bilshe_sered = 0
    for i in a:
        if i > serednie:
            bilshe_sered += 1

    with open("output.txt", "w") as t:
        t.write(
            f"Days: {kilkist}\nMin: {min}\nMax: {Max}\n"
            f"Average: {serednie}\nBilshe Sered: {bilshe_sered}"
        )