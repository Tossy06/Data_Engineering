def discount(precio, porcentaje_decuento):
    descuento = precio * (porcentaje_decuento/100)
    precio_final = precio - descuento
    return precio_final

precio_original = 100
porcentaje_descuento = 20

print(f'El precio final es: {discount(precio_original, porcentaje_descuento)}')

