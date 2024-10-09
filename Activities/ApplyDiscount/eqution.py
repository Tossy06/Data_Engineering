from sympy import symbols, Eq, solve

x= symbols('x')

ecuacion = Eq(2*x + 5, 15)

solucion = solve(ecuacion, x)

print(f"La sulución de la ecuación {ecuacion} es: x = {solucion[0]}")