from sympy import symbols, Eq, solve

x, y = symbols('x y')

equation_1 = Eq(x + y, 6)
equation_2 = Eq(2*x - y, 4)

solucion = solve((equation_1, equation_2), (x, y))

print(f"Las soluciones son: x = {solucion[x]}, y = {solucion[y]}")