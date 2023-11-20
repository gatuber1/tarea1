num1=int(input("Ingrese un numero entero: "));
num2=int(input("Ingrese otro numero entero: "));
num3=int(input("Ingrese otro numero entero: "));
suma=int(num1+num2+num3)
promedio=int(suma//3)
if promedio % 2 == 0:
    print("El promedio es ",promedio," y es un numero par");
else:
    print("El promedio es ",promedio," y es un numero impar");