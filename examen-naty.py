#diccionario productos

productos = {'8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
'2175HD': ['lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
'123FHD': ['lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
'342FHD': ['lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050'], …
}

#stock = {modelo: [precio, stock], ...]

stock = {'8475HD': [387990,10], '2175HD': [327990,4], 'JjfFHD': [424990,1],
'fgdxFHD': [664990,21], '123FHD': [290890,32], '342FHD': [444990,7],
'GF75HD': [749990,2], 'UWU131HD': [349990,1], 'FS1230HD': [249990,0], ...
}




# Opción 1

def stock_marca (marca):
    total_stock = 0
    for stock in productos:
        if productos[stock][1] == marca.lower():
            total_stock += stock 



# Opción 2 Búsqueda por precio

def busqueda_precio (precio_min, precio_mx):
    try:
        precio_min =int (precio_min)
        precio_mx = int (precio_mx)
    except ValueError:
        print("Debe ingresar un valor entero")
        return
    
    lista_productos = [] 
    for stock (precio,stock) in stock.items():
        if precio_min <= precio <= precio_mx and stock > 0:
            nombre = productos [stock]
            lista_productos.append(f"{nombre},{stock}")  
    if lista_productos:
        lista_productos.sort()
        print("Productos en ese rango de precios")
        for producto, productos in lista_productos:
            print(f"{producto}")
    else:
        print("No hay productos en ese rango de precios")

# Opción 3 Actualizar precio
def actualizar_precio (stock, modelo_precio):
    if stock in stock_marca:
        stock_marca[stock] = modelo_precio
        return True
    else:
        return False
    
def menu():
    while True:
            print("**********Menú principal*************")
            print("1.Stock marca")
            print("2.Búsqueda por precio")
            print("3.Actualizar precio")
            print("4.Salir")

            opcion = input ("Seleccione una opción")
            if opcion == "1":
                marca = ("Ingrese el nombre del producto")
                stock_marca (marca)
            elif opcion =="2":
                precio_minimo = input("ingrese precio minímo")
                precio_maximo = input("ingrese precio máximo")
                busqueda_precio(precio_minimo,precio_maximo)
            elif opcion == "3":
                while True:
                    marca = input ("Ingrese la marca del producto ").upper()
                    try:
                        nuevo_precio = int(input("Ingrese el nuevo precio"))
                        actualizado = actualizar_precio(stock,nuevo_precio)
                        if actualizado:
                            print("El precio se ha actualizado")
                        else:
                            print("")
                    except ValueError:
                        print("El precio debe ser entero")

                    continuar = input("Desea actuañizar otro producto (s/n)").lower()
                    if continuar != "s":
                        break
            elif opcion == "4":
                print("Programa finalizado")
                break
            else:
                print("Opción no válida, intente nuevamente")

                menu()




        




                         



 