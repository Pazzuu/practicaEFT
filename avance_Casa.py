def mostrar_menu():
    print("******* Menú Principal *******")
    print("1. Stock por catergoría")
    print("2. Búsqueda de productos por rango de precio")
    print("3. Actualizar precio de producto")
    print("4. Agregar producto")
    print("5. Eliminar producto")
    print("6. Salir")
    print("*******************************")

def leer_opcion():
    while True:
        try:
            op = int(input("Ingrese una opción a realizar: "))
            if op < 1 or op > 6:
                raise ValueError
            else:
                return op
        except:
            print("Error: Ingrese un número entero positivo del 1 al 6.")


        
def validar_nombre(nombre_producto):
    return nombre_producto.strip() != ""

def validar_categoria(categoria):
    return categoria.strip() != ""

def validar_tamano(tamano):
    return tamano.strip().lower() in ['chico', 'mediano', 'grande']

def validar_leche(tipo_leche):
    return tipo_leche.strip() != ""

def validar_temporada(es_temporada):
    return tamano.strip().lower() in ['s','n']

def validar_precio(precio):
    if precio.isdigit():
        validar = int(precio)
        return validar > 0
    return False

def validar_stock(stock_disponible):
    if stock_disponible.isdigit():
        validar = int(stock_disponible)
        return validar >= 0
    return False


    
