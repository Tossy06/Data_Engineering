def average(ventas):
    if len(ventas) == 0:
        return 'No se ingresaron ventas, por favor ingrese al menos un valor.'
    
    suma = sum(ventas)
    promedio = suma / len(ventas)
    return promedio

ventas_acumuladas = []

while True:
    try:

        ventas = input('Ingrese las ventas diarias  o escriba "salir" para termianar: ')

        if ventas.lower() == 'salir':
            print('Saliendo del programa...')
            break
        lista_ventas = [float(i) for i in ventas.split()]
        ventas_acumuladas.extend(lista_ventas)

    except ValueError:
        print('Error: Por vaor, ingrese solo números válidos')

print(f'El promedio de las ventas diarias es: {average(ventas_acumuladas)}')