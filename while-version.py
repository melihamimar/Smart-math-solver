from sympy import *

x = symbols('x')

expr=sympify(input("Denkleminiz:"))
while True:
    print("==== Math assistant ====")
    print("1 - Denklem çöz")
    print("2- türev al")
    print("3- integral hesapla")
    print("4- Yeni denklem gir")
    print("5- Çıkış")

    

    secim=input("seçiminiz:")

    if secim=="5":
        break

    if secim == "1":
        print("çözüm:", solve(expr))

    elif secim=="2":
        print("türev:", diff(expr))

    elif secim=="3":
        print("integral:", integrate(expr))

    elif secim=="4":
        expr=sympify(input("Yeni denkleminiz:"))
        continue
 

    
