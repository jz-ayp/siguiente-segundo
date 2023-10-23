"""
Calcular la hora correspondiente al siguiente segundo
"""

# Entradas
horas = int(input("Hora: "))
minutos = int(input("Minutos: "))
segundos = int(input("Segundos: "))

# Proceso
segundos += 1
if segundos > 59:
    segundos = 0
    minutos += 1
    if minutos > 59:
        minutos = 0
        horas += 1
        if horas > 23:
            horas = 0
tiempo = f'{horas:02d}:{minutos:02d}:{segundos:02d}'

# Salidas
print('Hora al siguiente segundo >', tiempo)