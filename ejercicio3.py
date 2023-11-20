num1=int(input("Ingrese un numero entero: "));
num2=int(input("Ingrese un otro numero entero: "));
num3=int(input("Ingrese un otro numero entero: "));
suma=int(num1+num2+num3)
if suma % 7 == 0:
    print(suma," es múltiplo de 7")
else:
    print(suma," no es múltiplo de 7")