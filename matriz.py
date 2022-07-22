n=t=0
while n<=0:
    n=int(input("Ingrese el numero de columnas:"))
while t<=0:
    t=int(input("Ingrese el numero de filas:"))
print(" |",end="")
for i in range(1,t+1):
	for j in range(1,n+1):
		print('{:3}'.format(i*j), end=' ')
	print()
