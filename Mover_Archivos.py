import os
import shutil

# Crear la carpeta Proyecto111
proyecto_folder = "Proyecto111"
os.makedirs(proyecto_folder, exist_ok=True)

# Abrir Visual Studio Code en la carpeta Proyecto111
os.system("code " + proyecto_folder)

# Definir las rutas de origen y destino
from_dir = os.path.join(os.path.expanduser("~"), "Descargas")
to_dir = os.path.join(os.path.expanduser("~"), "Documentos_Archivos")

# Obtener la lista de archivos en la carpeta de origen
list_of_files = os.listdir(from_dir)
print("Archivos en la carpeta de origen:")
print(list_of_files)

# Recorrer la lista de archivos
for filename in list_of_files:
    # Obtener el nombre y la extensión del archivo
    name, extension = os.path.splitext(filename)
    # Comentar el estado anterior
    # print(f"Nombre: {name}, Extensión: {extension}")

# Imprimir mensaje de finalización
print("Proceso de lectura de archivos completado.")
