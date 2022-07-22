dinero=años=interes=0
while(dinero<500):
    dinero=float(input("Ingrese la cantidad de dinero inicial"))
while(años<=0):
    años=int(input("Ingrese el tiempo(años):"))
while(interes<=0 or interes>10):
    interes=float(int("Ingrese el interes:"))
for i  in range(1,años*12+1):
    dinero+=(dinero*interes)/100
print(f"total de la poliza:{round(dinero,2)}")
