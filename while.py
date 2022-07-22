print("factorial")
a=0
suma=0
while a>-1:
    print("Ingrese el valor de A:")
    a=int(input(" "))
    if a>0 and a<10 :
        num=0
        factorial=1
        for num in range(a):
            factorial=factorial*(num+1)
        suma=suma+factorial
        print("Resultado:",factorial)
print("Resultado suma:",suma)

