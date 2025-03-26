from cipher import encrypt, decrypt
from utils import validate_key

def process_file():
    try:
        action = input("¿Cifrar (C) o Descifrar (D)? ").upper()
        if action not in ("C", "D"):
            print("Opción no válida.")
            return
        
        file_path = input("Ruta del archivo (ej: documento.txt): ").strip()
        key = validate_key(input("Clave: "))
        
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        result = encrypt(content, key) if action == "C" else decrypt(content, key)
        
        output_path = f"{file_path.split('.')[0]}_{'cifrado' if action == 'C' else 'descifrado'}.txt"
        with open(output_path, 'w', encoding='utf-8') as file:
            file.write(result)
        
        print(f"\n✅ Archivo procesado. Guardado como: {output_path}")
    
    except FileNotFoundError:
        print(" Error: Archivo no encontrado.")
    except Exception as e:
        print(f" Error inesperado: {e}")