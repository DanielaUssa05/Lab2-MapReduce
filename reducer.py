
#!/usr/bin/env python3
import sys
import math

categoria_actual = None
cantidad = 0
promedio = 0.0
m2 = 0.0

def mostrar_resultado():
    categoria, subcategoria = categoria_actual
    desviacion = math.sqrt(max(0.0, m2 / cantidad))

    print(
        f"{categoria}\t{subcategoria}\t"
        f"{promedio:.2f}\t{desviacion:.2f}\t{cantidad}"
    )

print("Categoria\tSubcategoria\tPromedio\tDesviacion\tCantidad")

for linea in sys.stdin:
    datos = linea.strip().split("\t")

    if len(datos) != 3:
        continue

    categoria, subcategoria, valor = datos
    clave = (categoria, subcategoria)

    try:
        valor = float(valor)
    except ValueError:
        continue

    if clave != categoria_actual:
        if categoria_actual is not None:
            mostrar_resultado()

        categoria_actual = clave
        cantidad = 0
        promedio = 0.0
        m2 = 0.0

    cantidad += 1
    diferencia = valor - promedio
    promedio += diferencia / cantidad
    diferencia2 = valor - promedio
    m2 += diferencia * diferencia2

if categoria_actual is not None:
    mostrar_resultado()
