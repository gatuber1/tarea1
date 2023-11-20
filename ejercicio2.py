num1=int(input("Ingrese un numero entero: "))
num2=int(input("Ingrese un otro numero entero: "))
num3=int(input("Ingrese un otro numero entero: "))

if num2 >num1:
    num1 = num2
if num3 > num1:
    num1 = num3

print("El número mayor es:", num1)
