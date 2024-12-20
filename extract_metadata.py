import os
import exiftool
import json

def extract_metadata(file_name):
    # Construir la ruta completa al archivo en el directorio actual
    current_dir = os.getcwd()
    file_path = os.path.join(current_dir, file_name)

    # Verificar si el archivo existe
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File '{file_name}' not found in the current directory.")

    # Extraer metadatos
    with exiftool.ExifTool() as et:
        # Ejecutar el comando de extracción de metadatos
        metadata = et.execute(b"-j", file_path.encode("utf-8"))
        # Convertir el resultado de bytes a una cadena JSON
        metadata_json = json.loads(metadata)
    return metadata_json

if __name__ == "__main__":
    file_name = "foto1.jpg"  # Nombre del archivo a analizar en el directorio actual
    try:
        metadata = extract_metadata(file_name)
        print("Metadata extracted successfully:")
        for item in metadata:
            for key, value in item.items():
                print(f"{key}: {value}")
    except FileNotFoundError as e:
        print(e)
    except Exception as e:
        print(f"An error occurred: {e}")
