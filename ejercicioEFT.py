def mostrar_menu():
    print("=========== Menú Principal =========")
    print("1. Stock por catergoría")
    print("2. Búsqueda de productos por rango de precio")
    print("3. Actualizar precio de producto")
    print("4. Agregar producto")
    print("5. Eliminar producto")
    print("6. Salir")
    print("===================================")

def leer_opcion():
    while True:
        try:
            opcion = int(input("Ingrese una opción: "))
            if 1 <= opcion <= 6:
                return opcion
            else:
                print("Debe seleccionar una opción válida")
        except ValueError:
            print("Debe seleccionar una opción válida")

def stock_categoria(categoria, productos, ventas):
    total_stock = 0
    for codigo, datos in productos.items():
        if datos[1].lower() == categoria.lower():
            total_stock += ventas[codigo][1]
    print(f"El total de stock disponible es: {total_stock}")

def busqueda_precio(precio_min, precio_max, productos, ventas):
    resultados = []
    for codigo, datos_venta in ventas.items():
        precio = datos_venta[0]
        stock = datos_venta[1]
        if precio_min <= precio <= precio_max and stock != 0
            nombre_producto = productos[codigo][0]
            resultados.append(f"{nombre_producto}--{codigo}")
    if len(resultados) == 0:
        print("No hay productos en ese rango de precios.")
    else:
        resultados_ordenados = sorted(resultados)
        print(f"Los productos encontrados son: {resultados_ordenados}")

def buscar_codigo(codigo, ventas):
    return codigo in ventas

def actualizar_precio(codigo, nuevo_precio, ventas):
    if buscar_codigo(codigo, ventas):
        ventas[codigo][0] = nuevo_precio
        return True
    else:
        return False

def validar_texto_no_vacio(texto):
    return texto.strip() != ""

def validar_entero_positivo(valor_texto):
    try:
        valor = int(valor_texto)
        return valor > 0
    except ValueError:
        return False

def validar_entero_no_negativo(valor_texto):
    try:
        valor = int(valor_texto)
        return valor >= 0
    except ValueError:
        return False

def validar_tamano(tamano_texto):
    return tamano_texto in ("chico", "mediano", "grande")

def validar_es_temporada(respuesta):
    return respuesta in("s", "n")


def agregar_producto(codigo, nombre_producto, categoria, tamano, tipo_leche, es_temporada, precio, stock_disponible, productos, ventas):
    if codigo in productos:
        return False
    productos[codigo] = [nombre_producto, categoria, tamano, tipo_leche, es_temporada]
    ventas[codigo] = [codigo, stock_disponible]
    return True

def eliminar_producto(codigo, productos, ventas)
    if buscar_codigo(codigo_ventas):
        del productos[codigo]
        del ventas[codigo]
        return True
    else:
        return False

def mostrar_menu():
    print("========== MENÚ PRINCIPAL ==========")
    print("1. Stock por categoría")
    print("2. Búsqueda de productos por rango de precio")
    print("3. Actualizar precio de producto")
    print("4. Agregar producto")
    print("5. Eliminar producto")
    print("6. Salir")
    print("=====================================") 

productos = {
    'P001': ['Capuccino Clásico', 'cafe', 'mediano', 'entera', False],
    'P002': ['Latte Vainilla', 'cafe', 'grande', 'descremada', True],
    'P003': ['Té Verde Helado', 'te', 'mediano', 'sin leche', False],
    'P004': ['Mocha Avellana', 'cafe', 'grande', 'entera', True],
    'P005': ['Chocolate Caliente', 'bebida', 'chico', 'entera', False],
    'P006': ['Té Chai Latte', 'te', 'mediano', 'descremada', True],
}

ventas = {
    'P001': [2500, 15],
    'P002': [3200, 0],
    'P003': [2800, 10],
    'P004': [3500, 4],
    'P005': [2200, 7],
    'P006': [3100, 9],
}

continuar = True
while continuar:
    mostrar_menu()
    opcion = leer_opcion()

    if opcion == 1:
        categoria = input("Ingrese categor{ia a consultar: ")
        stock_categoria(categoria, productos, ventas)

    elif opcion == 2:
        precio_min = None
        precio_max = None
        while precio_min is None or preico_max is None:
            try:
                precio_min = int(input("Ingrese precio mínimo: "))
                precio_max = int(input("Ingrese precio máximo: "))
            except ValueError:
                print("Debe ingresar valores enteros")
                precio_min = None
                precio_max = None
        busqueda_precio(precio_min, precio_max, productos, ventas)

    elif opcion == 3:
        repetir = "s"
        while repetir == "s":
            codigo = input("Ingrese código del producto: ").upper()
            nuevo_precio_valido = False
            while not nuevo_precio_valido:
                nuevo_precio_texto = input("Ingrese nuevo precio: ")
                if validar_entero_positivo(nuevo_precio_texto):
                    nuevo_precio = int(nuevo_precio_texto)
                    nuevo_precio_valido = True
                else:
                    print("El preico debe ser u nentero positivo.")
            if actualizar_precio(codigo, nuevo_precio, ventas):
                print("Precio actualizado.")
            else:
                print("El código no existe.")
            repetir = input("¿Desea actualizar otro precio?(s/n): ").lower()

    elif opcion == 4:
        
