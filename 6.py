a=int(input("Ingrese el valor:"))
acu=0
for i in range(1,a+1):
    print("1/",i**2,end="")
    acu=acu+(1/(i**2))
print()
print(acu)