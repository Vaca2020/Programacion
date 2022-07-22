def suma(*a):
    print("\nTipo de datos del argumento:",
          type(a))
    sum=0
    for n in a:
        sum+=n
        
    print("Suma:",sum)
suma(3,9,10,45,25)
suma(1)
suma(3,5)
