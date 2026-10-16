a = float(input("перша сторона трикутника "))
b = float(input("друга сторона трикутника "))
c = float(input("третя сторона трикутника "))
if (a <= 0 and b <= 0 and c <= 0) or a + b <= c or a + c <= b or b + c <= a:
    print("не існує такого трикутника")
else:
    print("такий трикутник існує")
    if a==b==c: print("правильний")
    elif a==b or a==c or b==c: print("рівнобедрений")
    else: print("не такий не сякий")
    print(f"периметр = {a+b+c:.02f}")
