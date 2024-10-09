#Imagina que tienes una fábrica de jugos y estás haciendo una mezcla de dos tipos de jugos para obtener una cierta cantidad con un sabor balanceado y a un costo específico. Digamos que tienes dos tipos de jugo:
#Jugo A cuesta $2 por litro.
#Jugo B cuesta $3 por litro.
#Tu objetivo es mezclar estos jugos para obtener exactamente 20 litros de jugo a un costo total de $52.

from sympy import symbols, Eq, solve

x, y = symbols('x y')

equiation_1 = Eq(x + y, 20)
equiation_2 = Eq(2*x + 3*y, 52)
solution = solve((equiation_1,equiation_2), (x,y))

print(f"The solution of the problem is: From juice A there are {solution[x]} liters and of the juice B there are {solution[y]} liters")