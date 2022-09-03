from re import X
x = input("digite un número ")
x = int(x)
y = input("digite otro número ")
y = int(y)
z = input("digite otro número ")
z = int(z)
if x > y:
    if x > z:
        m = x
        print("El número mayor es: "+str(m))
    else:
        m = z
        print("El número mayor es: "+str(m))
else:
    if y > z:
        m = y
        print("El número mayor es: "+str(m))
    else:
        m = z
        print("El número mayor es: "+str(m))