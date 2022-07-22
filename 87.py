base=exponen=0
while base<=0:
    base= int(input("Ingrese la base:"))
while exponen<=0:
    exponen= int(input("Ingrese el exponente:"))
resultado=base**exponen
print("La potencia es:",resultado)

resultado2=pow(base,exponen)
print("La potencia es:",resultado2)