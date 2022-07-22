
print("Ingrese primer numero:")
a=int(input(" "))
print("Ingrese segindo numero:")
b=int(input(" "))
if a==b    :
    print("Los numero no pueden ser iguales")
else:
    numeros=1
    suma=0
    promedio=0
    i=0
    limites=0
    while numeros>0:
        print("Ingrese numeros")
        numeros=int(input(" "))
        
        if numeros>a and numeros<b:
            suma=suma+numeros 
        if (numeros>0 and numeros<a) or numeros>b:
            i=i+1
            promedio=promedio+numeros
        if numeros==a or numeros==b:
            limites=limites+1
print("suma:",suma)
print("promedio:",promedio/i)
print("Limites:",limites)