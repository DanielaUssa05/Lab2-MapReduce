
#!/usr/bin/env python3
import sys
import csv

for row in csv.reader(sys.stdin):
    if len(row) != 3:
        continue

    categoria = row[0].strip()
    subcategoria = row[1].strip()
    valor = row[2].strip()

    if categoria.lower() == "categoria":
        continue

    try:
        valor = float(valor)
    except ValueError:
        continue

    print(f"{categoria}\t{subcategoria}\t{valor}")
