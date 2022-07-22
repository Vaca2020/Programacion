n=t=a=s=0

while n<=0:
    n=int(input("Tamaño del paquete:"))
while a<=0:
    a=int(input("Tamaño del paquete:"))
while s<=0:
    s=int(input("Tamaño del paquete:"))
while t<=0:
    t=int(input("Tamaño máximo de venta de envío:"))
print(" |",end="")
while t<=0:
    t=int(input("Tamaño máximo de venta de envío:"))
print(" |",end="")
while t<=0:
    t=int(input("Tamaño máximo de venta de envío:"))
print(" |",end="")
        
        
        
for i in range(1,11):
            print("\n",i*10,"|",end=" ")
for j in range(1,11):
        		print('{:3}'.format(i*j), end=' ')
print()