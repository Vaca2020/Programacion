numero=100#define numeros
sumainter=0#define suma
contador1=0#define contador1
contador2=1#define contador 1
suma1=0#define suma
while True:#mientras
    num1=int(input("Ingrese el primer número: "))#Te pedi escribir el numero
    num2=int(input("Ingrese el segundo número: "))#Te pide escribir el segundo numero
    if num1==num2:#si son iguales
        print("error los numeros son iguales")#te escribe error
    else:
        break
if num1>num2:#condicion entre numeros
    minimo=num2#condicion entre maximos y minimos
    maximo=num1#igualdad entre minimos y maximos
else:
    minimo=num1#condicion
    maximo=num2#igualdad
while numero!=0:#no pertenece numeros a cero
    numero=int(input("ingrese un número "))#te pide numero
    if numero>minimo and numero<maximo:#calcula el rango del numero
        sumainter+=numero#opera la condicion
    elif numero<minimo or numero>maximo:#calcula el rango del numero
        suma1+=numero
        contador1+=1#opera la segunda condicion
    elif numero==minimo or numero==maximo:#calcula los ultimos rangos
        contador2+=1#opera la condicion
print("la suma de los numeros quu estan dentro es:",sumainter)#escribe la primera respuesta de los que pertenecen
print("el promedio de los numeros fuera del intervalo es: ",suma1/contador1)#escribe la respuesta de los que estan afuera
print("la cantidad de los numeros  ingresados iguales a los limites: ",contador2)#escribe la respuesta de los que son iguales
print("fin del programa ")