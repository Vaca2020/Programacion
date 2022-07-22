# -*- coding: utf-8 -*-
"""
Created on Thu Jun 16 09:37:25 2022

@author: angel
"""

while t<=0:
    t=int(input("Tamaño máximo de venta de envío:"))
print(" |",end="")
for i in range(1,t+1):
    print(f"\t{n*i}",end="")
    print("*i",end="")
print()
for i in range (1,t*10):
    print("-",end="")
print()
for i in range (1,11):
    print("\n",i*10,"|",end=" ")
    for j  in range (1,t+1):
        print(round((j*n)/(i*10),1),end=" ")