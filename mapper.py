import datetime
import sys 
from collections import Counter

inicio = 8   # 08:00
fin = 18     # 18:00 (inclusive)
horasfuera = Counter()

filename = sys.argv[1]
with open(filename, 'r') as f:
    for line in f:
        try:
            # Ejemplo de línea: 2025-07-20 07:15:02 usuario:ana
            timestamp_str, user_str = line.strip().split(" usuario:")
            timestamp = datetime.datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S")
            hour = timestamp.hour

            if hour < inicio or hour >= fin:
                usuario = user_str.strip()
                horasfuera[usuario] += 1
        except Exception as e:
            print(f"Error procesando linea: {line.strip()} - {e}")
# Guarda resultados en archivo .out

with open(f"{filename}.out", 'w') as out:
    for usuario, count in horasfuera.items():
        out.write(f"{usuario} {count} //numero de accesos fuera del area laboral \n")
