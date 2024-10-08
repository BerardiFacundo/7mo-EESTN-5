# Creamos un diccionario con los nombres de tres productos y su precio
productos = {
    "Manzana": 0.5,
    "Pan": 1.0,
    "Leche": 1.5
}

# Función que calcula el total a pagar si se compran ciertos productos
def calcular_total(compra):
    total = 0
    for producto, cantidad in compra.items():
        if producto in productos:
            total += productos[producto] * cantidad
    return total

# Ejemplo de compra
compra = {
    "Manzana": 4,
    "Pan": 2,
    "Leche": 1
}

# Calculamos el total a pagar
total = calcular_total(compra)
print(f"El total a pagar es: ${total}")
