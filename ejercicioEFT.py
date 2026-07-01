productos = {
'P001': ['Capuccino Clásico', 'cafe', 'mediano', 'entera', False],
'P002': ['Latte Vainilla', 'cafe', 'grande', 'descremada', True],
'P003': ['Té Verde Helado', 'te', 'mediano', 'sin leche', False],
'P004': ['Mocha Avellana', 'cafe', 'grande', 'entera', True],
'P005': ['Chocolate Caliente', 'bebida', 'chico', 'entera', False],
'P006': ['Té Chai Latte', 'te', 'mediano', 'descremada', True]
}
ventas = {
'P001': [2500, 15],
'P002': [3200, 0],
'P003': [2800, 10],
'P004': [3500, 4],
'P005': [2200, 7],
'P006': [3100, 9]
}

def mostrar_menu():
    print("===== MENÚ PRINCIPAL =====")
    print("1. Stock por categoria")
    print("2. Búsqueda de productos por rango de precio")
    print("3. Actualizar precio de producto")
    print("4. Agregar producto")
    print("5. Eliminar producto")
    print("6. Salir")
    print("==========================")

def ingresar_opcion():
    while True:
        try:
            op = int(input("Ingrese opcion que desee realizar"))
            if op < 1 or op > 6:
                raise ValueError
            else:
                return op
        except:
            print("Error: Ingrese un número entero del 1 al 6")


        
