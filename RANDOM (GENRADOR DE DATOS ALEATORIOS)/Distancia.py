import pandas as pd
import random

df = pd.read_csv("Ciudades.csv")

fila = df.sample(1).iloc[0]

print("=== Selección aleatoria ===")
print(f"ID: {fila['id']}")
print(f"Ciudad: {fila['ciudad']}")
print(f"Estado: {fila['estado']}")
print(f"Latitud: {fila['latitud']}")
print(f"Longitud: {fila['longitud']}")
print(f"Distancia KM: {fila['distancia_km']}")
print(f"Tiempo Horas: {fila['tiempo_horas']}")
