from sympy import symbols, Eq, solve
import matplotlib.pyplot as plt
import numpy as np

x, y = symbols('x y')

equation_1 = Eq(x + y, 6)
equation_2 = Eq(2*x - y, 4)

solucion = solve((equation_1, equation_2), (x, y))

print(f"Las soluciones son: x = {solucion[x]}, y = {solucion[y]}")


# Despejar y en ambas ecuaciones
y1 = solve(equation_1, y)[0]  # y1 = 6 - x
y2 = solve(equation_2, y)[0]  # y2 = 2*x - 4

# Crear un rango de valores de x para graficar
x_vals = np.linspace(-10, 10, 400)

# Calcular los valores correspondientes de y para cada ecuación
y_vals_1 = [y1.subs(x, val) for val in x_vals]  # y = 6 - x
y_vals_2 = [y2.subs(x, val) for val in x_vals]  # y = 2*x - 4

# Crear la figura y los ejes de la gráfica
plt.figure(figsize=(8, 6))

# Graficar las dos ecuaciones
plt.plot(x_vals, y_vals_1, label="x + y = 6", color="blue")
plt.plot(x_vals, y_vals_2, label="2x - y = 4", color="red")

# Graficar la solución como un punto
plt.scatter([solucion[x]], [solucion[y]], color="green", zorder=5, label=f"Solución: ({solucion[x]}, {solucion[y]})")

# Añadir etiquetas y leyenda
plt.xlabel("x")
plt.ylabel("y")
plt.axhline(0, color="black",linewidth=0.5)
plt.axvline(0, color="black",linewidth=0.5)
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.legend()
plt.title("Gráfica de las ecuaciones lineales")
plt.show()
