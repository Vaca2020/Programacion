def keyw(**datos):
    print("\nTipo de dato del argumento:",
          type(datos))
    for key, value in datos.items():
        print("{}is{}".format(key,value))
keyw(Firstname="Jaun",
     Lastname="Dominguez",
     Age=42,
     Phone=124578954)
keyw(Firstname="Jhon",
     Lastname="Wood",
     Email="johnwood@nomail.com",
     Contry="Wakanda",
     Age=25)
