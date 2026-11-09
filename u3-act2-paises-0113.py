
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

esp = ['España', 'Madrid', True, 47.4]
mex = ['México', 'CDMX', False, 126.7]
fra = ['Francia', 'París', True, 67.7]
arg = ['Argentina', 'Buenos Aires', False, 45.8]
jap = ['Japón', 'Tokio', False, 125.7]

# Creamos una lista de listas
lista_paises = [esp, mex, fra, arg, jap]

# Creamos el DataFrame
df_paises = pd.DataFrame(
    lista_paises,
    columns=["pais", "capital", "pertenece_UE", "poblacion"]
)

# Mostramos la tabla
print(df_paises)

# Creamos y guardamos el archivo CSV
df_paises.to_csv("paises.csv", index=False)

print("Archivo CSV guardado correctamente")

# Crear grafica de lineas
# donde x es pais en el eje horizontal
# donde y es poblacion en el eje vertical
plt.plot(df_paises["pais"], df_paises["poblacion"])
plt.title("Grafica de poblacion de paises 0113")
plt.xlabel("Nombre de los paises")
plt.ylabel("Poblacion en millones")
plt.show()

# Creamos una grafica de puntos
plt.scatter(df_paises["pais"], df_paises["poblacion"])
plt.show()

# Graficas de barra
plt.bar(df_paises["pais"], df_paises["poblacion"])
plt.title("Grafica de poblacion de paises 0113")
plt.xlabel("Nombre de los paises")
plt.ylabel("Poblacion en millones")
plt.show()

# Ordenar la grafica de barras de manera descendente
# De la mas grande a la mas pequeña
df_paises_ordenar = df_paises.sort_values("poblacion", ascending=False)
plt.bar(df_paises_ordenar["pais"], df_paises_ordenar["poblacion"])
plt.show()

# Coloreando la grafica
df_paises_ordenar = df_paises.sort_values("poblacion", ascending=False)
plt.bar(df_paises_ordenar["pais"], df_paises_ordenar["poblacion"],
        color=["b", "g", "c", "m", "y"])
plt.show()

# Grafica de pastel
plt.pie(df_paises["poblacion"], labels=df_paises["pais"],
        autopct="%1.1f%%")
plt.title("Poblacion de los paises 0113")
plt.show()
